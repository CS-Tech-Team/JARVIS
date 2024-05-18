import pyaudio
import webrtcvad
from faster_whisper import WhisperModel
import numpy as np
import threading
import time
from sys import exit
from queue import Queue
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

class LiveWhisper:
    exit_event = threading.Event()

    def __init__(self, model_name, device_name="default", speech_threshold=0.5):
        self.model_name = model_name
        self.device_name = device_name
        self.speech_threshold = speech_threshold

    def stop(self):
        """stop the asr process"""
        LiveWhisper.exit_event.set()
        self.asr_input_queue.put("close")
        print("ASR stopped")

    def start(self):
        self.asr_output_queue = Queue()
        self.asr_input_queue = Queue()
        self.asr_process = threading.Thread(target=LiveWhisper.asr_process, args=(
            self.model_name, self.asr_input_queue, self.asr_output_queue, self.speech_threshold))
        self.asr_process.start()
        time.sleep(5)  
        self.vad_process = threading.Thread(target=LiveWhisper.vad_process, args=(
            self.device_name, self.asr_input_queue,))
        self.vad_process.start()

    @staticmethod
    def vad_process(device_name, asr_input_queue):
        vad = webrtcvad.Vad()
        vad.set_mode(1)

        audio = pyaudio.PyAudio()
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        FRAME_DURATION = 30
        CHUNK = int(RATE * FRAME_DURATION / 1000)

        microphones = LiveWhisper.list_microphones(audio)
        selected_input_device_id = LiveWhisper.get_input_device_id(
            device_name, microphones)

        stream = audio.open(input_device_index=selected_input_device_id,
                            format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)

        frames = b''
        while True:
            if LiveWhisper.exit_event.is_set():
                break
            frame = stream.read(CHUNK, exception_on_overflow=False)
            is_speech = vad.is_speech(frame, RATE)
            if is_speech:
                frames += frame
            else:
                if len(frames) > 1:
                    asr_input_queue.put(frames)
                frames = b''
        stream.stop_stream()
        stream.close()
        audio.terminate()

    @staticmethod
    def asr_process(model_name, in_queue, output_queue, speech_threshold):
        model = WhisperModel(model_name, device="cuda", compute_type="int8")

        print("\nListening to your voice\n")
        while True:
            audio_frames = in_queue.get()
            if audio_frames == "close":
                break

            float64_buffer = np.frombuffer(
                audio_frames, dtype=np.int16) / 32767
            start = time.perf_counter()
            segments, _ = model.transcribe(float64_buffer)
            text = ""
            for segment in segments:
                if segment.no_speech_prob < speech_threshold:
                    text += segment.text.lower()
            inference_time = time.perf_counter() - start
            sample_length = len(float64_buffer) / 16000  
            if text != "":
                output_queue.put([text, sample_length, inference_time])

    @staticmethod
    def get_input_device_id(device_name, microphones):
        for device in microphones:
            if device_name in device[1]:
                return device[0]

    @staticmethod
    def list_microphones(pyaudio_instance):
        info = pyaudio_instance.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')

        result = []
        for i in range(0, numdevices):
            if (pyaudio_instance.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                name = pyaudio_instance.get_device_info_by_host_api_device_index(
                    0, i).get('name')
                result += [[i, name]]
        return result

    def get_last_text(self):
        return self.asr_output_queue.get()


if __name__ == "__main__":
    
    print("Live ASR")
    asr = LiveWhisper("medium.en", speech_threshold=0.5)

    asr.start()

    try:
        while True:
            text, sample_length, inference_time = asr.get_last_text()
            print(f"{sample_length:.3f}s\t{inference_time:.3f}s\t{text}")

    except KeyboardInterrupt:
        asr.stop()
        exit()

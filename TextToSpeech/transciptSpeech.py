import wave 
import pyaudio
from faster_whisper import WhisperModel 
import os 

RATE = 16000
CHUNK = 1024
CHANNELS = 1
FORMAT = pyaudio.paInt16


def transcribe_chunk(model, chunk_file):
    segments, _ = model.transcribe(chunk_file)
    res = ""
    for segment in segments:
        if segment.no_speech_prob < 0.5:
            res += segment.text
    return res

def record_chunk(p, stream, file_path, chunk_length=3):
    frames = []
    for i in range(0, int(RATE / CHUNK * chunk_length)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
    
def main():
    model_size = "medium.en"
    model = WhisperModel(model_size, device="cuda", compute_type="int8")
    
    p = pyaudio.PyAudio()
    
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

    device_id = int(input("Enter input device id: "))

    
    stream = p.open(format=pyaudio.paInt16, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, input_device_index=device_id)
    
    accumulated_transcription = ""
    
    try:
        while True:
            chunk_File = "temp_chunk.wav"
            record_chunk(p, stream, chunk_File)
            
            transcription = transcribe_chunk(model, chunk_File)
            
            if len(transcription) > 0:
                print(transcription)
            
            os.remove(chunk_File)
        
            accumulated_transcription += transcription
    except KeyboardInterrupt:
        print("Final transcription: ", accumulated_transcription)
        stream.stop_stream()
        stream.close()
        p.terminate()
        exit()
    
    finally:
        print()
        
if __name__ == "__main__":
    main()
import keyboard
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
    
    stream = p.open(format=pyaudio.paInt16, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    accumulated_transcription = ""
        
    try:
        if keyboard.is_pressed('s'):
            stream = p.open(format=pyaudio.paInt16, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
            print("Listening...")
        while keyboard.is_pressed('s'):
            
            chunk_File = "temp_chunk.wav"
            record_chunk(p, stream, chunk_File)
            
            transcription = transcribe_chunk(model, chunk_File)
            
            if len(transcription) > 0:
                print(transcription)
            
            os.remove(chunk_File)
        
            accumulated_transcription += transcription
            
        print(accumulated_transcription)
        accumulated_transcription = ""  
        stream.stop_stream()
        stream.close()  
        
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
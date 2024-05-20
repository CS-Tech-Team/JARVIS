import threading
import queue
from .whisper_speech_recognition import LiveWhisper

class LiveWhisperListener:
    def __init__(self, model_name="medium.en", device_name="default", speech_threshold=0.5):
        self.asr = LiveWhisper(model_name, speech_threshold=speech_threshold, device_name=device_name)

    def start(self, q):
        self.asr.start()
        try:
            while True:
                text, sample_length, inference_time = self.asr.get_last_text()
                if text:
                    q.put(text)
        except KeyboardInterrupt:
            self.asr.stop()
            exit()

def speech_listener(q, model_name="medium.en", device_name="default", speech_threshold=0.6):
    listener = LiveWhisperListener(model_name=model_name, device_name=device_name, speech_threshold=speech_threshold)
    listener.start(q)

def speech_listener_thread(q):
    listener_thread = threading.Thread(target=speech_listener, args=(q,))
    listener_thread.daemon = True
    listener_thread.start()

if __name__ == "__main__":
    newq = queue.Queue()
    
    # listener_thread = threading.Thread(target=speech_listener, args=(newq,))
    # listener_thread.daemon = True
    # listener_thread.start()
    
    speech_listener_thread(newq)
    
    while True:
        try:
            text = newq.get()  # Wait for new text with a timeout
            print(f"Received text: {text}")
        except queue.Empty:
            print("No new text received.")

import queue
import threading
import os

from SpeechToText import speech_listener_thread

speech_results_q = queue.Queue()
speech_listener_thread(speech_results_q)

while True:
    try:
    
        for thread in threading.enumerate():
            print(f"Thread Name: {thread.name}, Thread ID: {thread.ident}")
        
    
    
        text = speech_results_q.get()  # Wait for new text with a timeout
        
    
    
        if "close" in text:
            os._exit(-1)
        
        
        print(f"User: {text}")



    except queue.Empty:
        print("No new voice received.")

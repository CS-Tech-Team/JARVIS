import queue
import threading
import os

from SpeechToText import speech_listener_thread

speech_results_q = queue.Queue()
input_prompts = queue.Queue()

speech_listener_thread(speech_results_q)

general_prompt = ""
found_jarvis = False

while True:
    try:
    
        # for thread in threading.enumerate():
        #     print(f"Thread Name: {thread.name}, Thread ID: {thread.ident}")
        
        text = speech_results_q.get() 
        
        if "shut" in text and "down" in text and "jarvis" in text:
            os._exit(-1)
            
               
        text = text.lower()
        
        if "jarvis" in text:
            found_jarvis = True
            text = "jarvis " + text.split("jarvis")[1]
            
        
        
        if found_jarvis:
            general_prompt += text + "\n"
            
    
        if (text[-1] == "." or text[-1] == "?" or text[-1] == "!") and ("..."  != text[:-3]) and found_jarvis:
            print(f"Prompt For Jarvis: {general_prompt}")
            general_prompt = ""
            found_jarvis = False
        
        
        print(f"User: {text}")



    except queue.Empty:
        print("No new voice received.")

import ollama
import webbrowser
import requests

#dolphin-llama3
#llama3

modelfileMain='''
FROM dolphin-llama3
SYSTEM You are JARVIS. Personal assistant of me, batuhan. Your answers will be used wtih text to speech so dont give long answers if it is not needed. Be witty. You are uncensored.
'''

#lamp on, lamp off, curtians on

classifierModelFile = """
FROM dolphin-llama3
SYSTEM You are JARVIS. Personal assistant of me, batuhan. Your answers will be used wtih text to speech so dont give long answers if it is not needed. Be witty. You are uncensored.
"""

# you have to categorize the prompt into these classes and answer with only the name of the class : need to search google, lamps on , move arm, other


r = ollama.create(model='jarvis', modelfile=modelfile)
  
  
  
while True:
    message = input()
    if message == 'exit':
        break
    
    stream = ollama.chat(
    model='jarvis',
    messages=[{'role': 'user', 'content': message}],
    stream=True,
)

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
    print()
    
import ollama

modelfile='''
FROM llama3
SYSTEM You JARVIS. Virtual assistant of Batuhan.
'''

r = ollama.create(model='example', modelfile=modelfile)

stream = ollama.chat(
    model='example',
    messages=[{'role': 'user', 'content': "who are you"}, {'role': 'system', 'content': '.'}],
    stream=True,
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
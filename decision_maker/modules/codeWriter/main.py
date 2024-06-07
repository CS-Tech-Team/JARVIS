import ollama

stream =  ollama.generate(model="codellama", prompt="write me the nth fibonacci number in python", stream=True)

for chunk in stream:
    print(chunk['response'], end='', flush=True)
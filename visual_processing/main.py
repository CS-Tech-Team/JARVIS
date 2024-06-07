import ollama

stream = ollama.generate(model="llava", prompt="do you see any dangers out there ", images=["test.JPEG"], stream=True)

for chunk in stream:
    print(chunk['response'], end='', flush=True)
    


 
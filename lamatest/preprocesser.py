import ollama

moduleDetectionPrompt = open("firstPhasePrompt.txt", "r").read()
modules = open("modules.txt", "r").read().split("\n")


def getTheModule(prompt):

    stream = ollama.chat(
    model='phi3',
    messages=[{'role': 'user', 'content': prompt}, {'role': 'system', 'content': moduleDetectionPrompt}],
    stream=False,
    )

    res = stream['message']['content']
    for i in modules:
        if i.lower() in res.lower():
            return i
    
    
if __name__ == "__main__":

    while True:
        allocatedModule = ""
        message = input("You:")
        print(getTheModule(message))
        
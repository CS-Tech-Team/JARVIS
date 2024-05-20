import ollama
import utils

moduleDetectionPrompt = open("firstPhasePrompt.txt", "r").read()
modules = utils.readYaml("modules.yaml")["modules"]

def getTheModule(prompt):

    stream = ollama.chat(
    model='llama3',
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
        
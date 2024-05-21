import yaml
import ollama

def get_medias(yamlfile):
    with open(yamlfile) as stream:
        try:
            return yaml.safe_load(stream)["medias"]
        except yaml.YAMLError as exc:
            return exc
        
        
medias = get_medias("media_options.yaml")


systemPrompt = open("prompt.txt", "r").read()

mediasAsString = "\n".join([i for i in medias])

print(mediasAsString)

systemPrompt = systemPrompt.replace("((medias))", mediasAsString)


def getTheModule(prompt):

    stream = ollama.chat(
    model='llama3',
    messages=[{'role': 'user', 'content': prompt}, {'role': 'system', 'content': systemPrompt}],
    stream=False,
    )

    res = stream['message']['content']
    
    for i in medias:
        if i.lower() in res.lower():
            return i
    return res
    
if __name__ == "__main__":

    while True:
        allocatedModule = ""
        message = input("You:")
        print(getTheModule(message))
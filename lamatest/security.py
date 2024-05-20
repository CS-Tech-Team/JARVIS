import ollama

securityPrompt = open("security_devices.txt", "r").read()
devices = securityPrompt.split("Devices:\n\n")[1].split("\n======")[0].split("\n")


def getTheModule(prompt, sendRequestQueue):

    stream = ollama.chat(
    model='phi3',
    messages=[{'role': 'user', 'content': prompt}, {'role': 'system', 'content': securityPrompt}],
    stream=False,
    )

    res = stream['message']['content']
    
    device = None
    
    for i in devices:
        if i.lower() in res.lower():
            device = i  
            break

    if device == None:
        return "straight to JARVIS"
    
    elif device == "ElectroShock Device":
        return "start the electroShock device"
    
    elif device == "flamethrower":
        return "start the flameThrower"
    
    elif device == "face tracker":
        return "Start the Face Tracker"
    
    elif device == "other":
        return "Straight to JARVIS"
    
if __name__ == "__main__":

    while True:
        allocatedModule = ""
        message = input("You:")
        print(getTheModule(message))
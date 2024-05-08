import ollama

moduleDetectionPrompt = open("firstPhasePrompt.txt", "r").read()
modules = open("modules.txt", "r").read().split("\n")

# moduleDetectorModelFile = f'''
# FROM dolphin-llama3
# {moduleDetectionPrompt}'''


#r = ollama.create(model='modeuleDetector', modelfile=moduleDetectorModelFile)
# Home Automation
# Personal Assistant
# Entertainment and Media
# Navigation and Travel
# Shopping and Logistics
# Security and Monitoring
# Health and Wellness
# Educational and Informational
# Casual Talk  
  
while True:
    
    allocatedModule = ""
    
    message = input("You:")
    if message == 'exit':
        break
    
    stream = ollama.chat(
    model='dolphin-llama3',
    messages=[{'role': 'user', 'content': message}, {'role': 'system', 'content': moduleDetectionPrompt}],
    stream=True,
)

    print("=======")
    res = ""
    for chunk in stream:
        
        chunk['message']['content']
        res+=chunk['message']['content']
        
        foundModule = False
        
        for moduleName in modules:
            if moduleName in res:
                allocatedModule = moduleName
                print("Module: " + moduleName)
                res = ""
                foundModule = True
                break
            
        if foundModule:
            break
        
    
    if allocatedModule == "Home Automation":
        print("Home Automation Module")
    elif allocatedModule == "Web Browser":
        print("Web Browser Module")

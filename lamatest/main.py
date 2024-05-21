from preprocesser import getTheModule
import yaml

modules = open("modules.txt", "r").read().split("\n")
print(modules)
# ['Home Automation', 'Entertainment and Medias', 'Security and Monitoring', 'Weapons and Defense', 'Health and Wellness', 'Informational', 'google search module', 'wikipedia search module', 'other']

def main(prompt):
    main_pompt = prompt
    
    module = getTheModule(main_pompt)
    
    if module == "Home Automation":
        return "Home Automation Module"
    elif module == "Entertainment and Medias":
        return "Entertainment and Medias Module"
    elif module == "Security and Monitoring":
        return "Security and Monitoring Module"
    elif module == "Weapons and Defense":
        return "Weapons and Defense Module"
    elif module == "Health and Wellness":
        return "Health and Wellness Module"
    elif module == "Informational":
        return "Informational Module"
    elif module == "google search module":
        return "google search module Module"
    elif module == "wikipedia search module":
        return "wikipedia search module Module"
    elif module == "other":
        return "Directly to JARVIS himself"
    else:
        return "Directly to JARVIS himself"
    
    
if __name__ == "__main__":
    while True:
        prompt = input("Enter your prompt: ")
        print(main(prompt))
        print("\n\n")
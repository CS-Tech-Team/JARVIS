import ollama

moduleDetectionPrompt = open("firstPhasePrompt.txt", "r").read()
modules = open("modules.txt", "r").read().split("\n")


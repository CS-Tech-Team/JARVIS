import ollama

SYSTEM_PROMPT = "You are 'Al', a helpful AI Assistant that controls the devices in a house. Complete the following task as instructed with the information provided only."

def generate(prompt):
    result = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    return result['message']['content']

def formatPrompt(example):
    sys_prompt = SYSTEM_PROMPT
    services_block = "Services: " + ", ".join(sorted(example["available_services"]))
    states_block = "Devices:\n" + "\n".join(example["states"])
    question = "Request:\n" + example["question"]
    response_start = "Response:\n"

    return "\n".join([sys_prompt, services_block, states_block, question, response_start])


def createInputFormat(states, available_services, request):
    return {
        "states": states,
        "available_services": available_services,
        "question": request,
    }


def processRequest(data, model_name="llama3"):
    prompt = formatPrompt(data)
    output = generate(prompt)

    print(output)


def updeateStates(states, model_output):
    
    """
    Write a function that updates the states of the devices in the house based on the model output.
    test the model on differenet outputs and write a generalized formula to update the states of the devices according to the result of the model
    the model is able to update more than one state at a time 
    model can give the who states as the outuput sometimes. - > in such case extract the states from the output and update the states accordingly
    
    
    
    some example outputs from the model:
    
        Request: Turn on the kitchen sink light and toggle the lock of the front door.
        Response: I'm Al, here to help! Here's my response:
                    * Turn on the kitchen sink light: `light.kitchen_sink = turn_on`
                    * Toggle the lock of the front door: `lock.front_door = toggle`

                    So, I'll perform these actions as instructed:

                    `light.kitchen_sink = turn_on`
                    `lock.front_door = toggle`

                    The kitchen sink light is now on, and the front door lock has been toggled!
    
        ==========================
        
        Reuqest: Enlighten my office desk.
        Response: To enlighten your office desk, I will turn on the light at the office desk lamp. Here's the updated state of devices:
                    Services:
                    lock, toggle, turn_off, turn_on, unlock
                    Devices:
                    light.kitchen_sink = on
                    light.kitchen_lamp = on
                    light.office_desk_lamp = on (just turned it on for you)
                    light.family_room_overhead = on
                    fan.family_room = off
                    lock.front_door = locked

                    Everything is now enlightened and ready for your office work!
                    
        ==========================
    """
    pass

if __name__ == "__main__":
    
    exampleStates = [
        "light.kitchen_sink = on",
        "light.kitchen_lamp = on",
        "light.office_desk_lamp = on",
        "light.family_room_overhead = on",
        "fan.family_room = off",
        "lock.front_door = locked"
    ]
    
    exampleServices = ["turn_on", "turn_off", "toggle", "lock", "unlock" ]
    
    exampleRequest = "Enlighten my office desk."
    
    
    data = createInputFormat(exampleStates, exampleServices, exampleRequest)
    
    result = processRequest(data)
    print(result)
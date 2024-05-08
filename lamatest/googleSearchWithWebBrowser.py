import ollama
import webbrowser

SYSTEM_PROMPT = "You are 'Al', a helpful AI Assistant that can determine which term to search on google."


def generate(prompt):
    result = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    return result['message']['content']

def formatPromptSearch(example):
    sys_prompt = SYSTEM_PROMPT
    services_block = "Services: " + ", ".join(sorted(example["available_services"]))
    question = "Request:\n" + example["question"]
    term = "Search Term: \n"

    return "\n".join([sys_prompt, services_block, question, term])

def openGoogleOnBrowser(modelResult):
    
    """
    extract the searchTerm from modelResult
    
    replace the spaces in the search term with the "+" sign.
    
    open the browser and search the term on google with the following link:
        webbrowser.open("https://www.google.com/search?q=" + searchTerm.replace(" ", "+"))
    
    the llama model should not intervene the result of this function.
    
    return a string that says the search term is searched on google.
    
    """


def createInputFormat(available_services, request):
    return {
        "available_services": available_services,
        "question": request,
    }


def processRequest(data, model_name="llama3"):
    prompt = formatPromptSearch(data)
    output = generate(prompt)

    print(output)

if __name__ == "__main__":

    exampleServices = ["google search"]
    
    exampleRequest = "search Nural Networks on goole."
    
    data = createInputFormat(exampleServices, exampleRequest)
    
    result = processRequest(data)
    print(result)
    
    
"""
Further improvements:
    add ability to read the result pages and get the most releated one to out goal.
"""
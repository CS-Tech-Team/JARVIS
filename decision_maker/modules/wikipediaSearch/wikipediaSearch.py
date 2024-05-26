import ollama
import wikipedia

SYSTEM_PROMPT = "You are 'Al', a helpful AI Assistant that can determine which term to search on wikipedia and the goal of the search. Just write the goal and the wanted service and do not proceed more."


def generate(prompt):
    result = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    return result['message']['content']

def formatPromptSearch(example):
    sys_prompt = SYSTEM_PROMPT
    services_block = "Services: " + ", ".join(sorted(example["available_services"]))
    question = "Request:\n" + example["question"]
    term = "Search Term: \n"
    service = "Needed Service: \n"

    return "\n".join([sys_prompt, services_block, question, term, service])

def getInfo(modelResult):
    
    """
    extract the searchTerm from modelResult
    
    return the summary of the search key using:
        wikipedia.summary(searchTerm)
    
    the llama model should not intervene the result of this function.
    just return the summary of the search term.    
    
    """

def summerizeYourself(modelResult):
    
    """
    
    Extract the possible search term from the modelResult
    
    Get the content of the page with:
        wikipedia.page(searchKey).content
        
    give this content to the llama model and tell it to summarize the content.
    
    return the summrized content.    
    
        
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

    exampleServices = ["get info", "summarize"]
    
    exampleRequest = "What does it say about apollo program on wikipedia."
    exampleRequest2 = "Can you summirize me what it tells about apollo program on wikipedia."
    
    data = createInputFormat(exampleServices, exampleRequest)
    
    result = processRequest(data)
    print(result)
    
    
"""
Further improvements:
    add all the funcitonalities of the wikipedia library to this module which explained in the below link:
        https://www.geeksforgeeks.org/how-to-extract-wikipedia-data-in-python/
    
"""
import ollama
import wikipedia

SYSTEM_PROMPT = "You are 'Al', a helpful AI Assistant that can determine which term to search on wikpedia. The user will ask a question about a term that could be answered via wikipedia, i want you to extract that term and give me the term inside to asterics (**) so i w ill know which term to search. Just write the search term do no overcomplicate things."


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
    
    step 1 : Extract the possible search term from the modelResult
    
    step 2 : Get the content of the page with:
        wikipedia.page(searchKey).content
        
    step 3 : get the content of the page and give this content to the llama model and tell it to summarize the content.
            ollama.chat()
    
    step 4 : return the summrized content.    
    
        
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

    exampleServices = ["get info"]
    
    exampleRequest = "What does it say about apollo program on wikipedia."
    exampleRequest2 = "I want to study the life of George Washington on wikipedia."
    
    data = createInputFormat(exampleServices, exampleRequest2)
    
    result = processRequest(data)
    print(result)
    
    print(getInfo(result))
    print(summerizeYourself(result))
    
    
"""
Further improvements:
    add all the funcitonalities of the wikipedia library to this module which explained in the below link:
        https://www.geeksforgeeks.org/how-to-extract-wikipedia-data-in-python/
    
"""
import ollama
import webbrowser
import requests
import decision_maker.modules.googleSearch.search_api as search_api
from bs4 import BeautifulSoup

SYSTEM_PROMPT = "You are 'Al', a helpful AI Assistant that can determine which term to search on google.And term that you gave me is supposed to be between ** and ** not between 'and '. Like **searchterm**"


def generate(prompt):
    result = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    return result['message']['content']

def formatPromptSearch(example):
    sys_prompt = SYSTEM_PROMPT
    services_block = "Services: " + ", ".join(sorted(example["available_services"]))
    question = "Request:\n" + example["question"]
    term = "Search Term: \n"

    return "\n".join([sys_prompt, services_block, question, term])


def return_last_url_to_search_api(modelResult):
    search_term=modelResult.split("**")[1].replace(" ","+")
    return search_term
    

    
def openGoogleOnBrowser(link):
    
    webbrowser.open(link)
    
    
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

    return output

def analyze_link_to_access_content(searched_first_link):
    result =requests.get(searched_first_link)
    soup=BeautifulSoup(result.content,"html.parser")
    # print(soup.text.strip())
    return soup.text.strip()
    
    



if __name__ == "__main__":

    exampleServices = ["google search"]
    
    exampleRequest = "What is the date of invention of internet"
    
    data = createInputFormat(exampleServices, exampleRequest)
    
    result = processRequest(data)
    search_query=result.split("**")[1]
    search_query.replace('"',"")
   
    link=search_api.perform_google_search(search_query)
 
    
    print(link)
    
    openGoogleOnBrowser(link)
    
    content_of_link = analyze_link_to_access_content(link)
    
    print(content_of_link)
    
    

    # url=openGoogleOnBrowser(result)[0]
    
    
    
    
    
    
    # print(result)
    
    
    
"""
Further improvements:
    add ability to read the result pages and get the most releated one to out goal.
"""
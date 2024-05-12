import ollama
import webbrowser
import requests
from bs4 import BeautifulSoup

SYSTEM_PROMPT = "You are 'Al', a helpful AI Assistant that can determine which term to search on google.And term that you gave me is supposed to be between ** and **. Like **searchterm**"


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
    search_term=modelResult.split("**")[1].replace(" ","+")
    base_url="https://www.google.com/search?q="
    last_url=base_url+f"{search_term}"
    webbrowser.open(last_url)
    return last_url
    
    
    
    
    
    
    
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

def get_page(url):
    res=requests.get(url)
    html_page=BeautifulSoup(res.content,"lxml")
    
    searching_site=html_page.find("div",class_="dURPMd")
    print(searching_site)
    
    

if __name__ == "__main__":

    exampleServices = ["google search"]
    
    exampleRequest = "search when was internet invented on google."
    
    data = createInputFormat(exampleServices, exampleRequest)
    
    result = processRequest(data)

    # openGoogleOnBrowser(result)
    url=openGoogleOnBrowser(result)
    get_page(url)
    
    
    # print(result)
    
    
    
"""
Further improvements:
    add ability to read the result pages and get the most releated one to out goal.
"""
import requests
import googleSearchWithWebBrowser

def perform_google_search(search_query):
    API_KEY = "AIzaSyBJQNCSHr8zzx5hrKwiJ6ZgJHkBZHEAqFY"
    SEARCH_ENGINE_ID = "5222eeec54f014650"
    
    
    

    

    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_query,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID
    }
    response = requests.get(url, params=params)
    result = response.json()
    if 'items' in result:
        return  result['items'][0]["link"]
    



import requests
import decision_maker.modules.googleSearch.googleSearchWithWebBrowser as googleSearchWithWebBrowser

def perform_google_search(search_query):
    API_KEY = "APIKEY"
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
    



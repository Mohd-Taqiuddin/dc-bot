import os, json
from googleapiclient.discovery import build

with open('google_keys.json', 'r') as f:
    keys = json.load(f)
    # print(keys)
    f.close()

cse_key = keys["google_cse_key"]
cse_id = "a6baec900a47642f9"

# cse_key = "AIzaSyD9FYvFyh46hy4gNzBD1lJiM3vfeJqU4tA"
# cse_id = "884659769943-c45483qddeo031du4c72orqv606jge32.apps.googleusercontent.com"

def search_google(query, num_results=3):
    """
    returns a list of search results as URLs
    query: self explanatory
    num_results: how many URLs u want to send
    """

    temp = []
    service = build("customsearch", "v1", developerKey=cse_key)
    results = service.cse().list(q=query, cx=cse_id).execute()['items']
    for i in range(0, num_results):
        temp.append(results[i]['link'])
    return temp

def image_search(query, num_results=1):
    """
    returns a list of image URLs.
    query: self explanatory
    """

    temp = []
    service = build("customsearch", "v1", developerKey=cse_key)
    results = service.cse().list(q=query, cx=cse_id, searchType = "image").execute()['items']
    
    for i in range(0, num_results):
        temp.append(results[i]['link'])
    return temp
    
# print(search("holy panda", 2))
# print(image_search("holy panda"))

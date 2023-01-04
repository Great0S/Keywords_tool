import ast
import csv
import json
from serpapi import GoogleSearch
from config.settings import settings

logger = settings.logger
key = settings.serpApi_key5
params = None


def serp(query: str, lang: str):
    global params

    params = {
        "engine": "google",
        "q": query,
        "google_domain": "google.com",
        "lr": "lang_en|lang_tr",
        "filter": 0,
        "num": 100,
        "start": 0,
        "api_key": key,
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    results_total = results['search_information']['total_results']

    get_highlighted_keywords(query)


def get_highlighted_keywords(query):
    global params, hsnip, asnip, snip
    
    snip = None
    hsnip = []
    asnip = []
    data_header = ['position','query', 'snippet_highlighted_words', 'rich_snippet_list', 'snippet', 'link']
    data = []

    try:
        for page in range(0, 1000, 100):
            
             search = GoogleSearch(params)
             search.params_dict['start'] = page
             offset_results = search.get_dict()
             
             for result in offset_results["organic_results"]:
                if 'snippet_highlighted_words' in result:    
                    for sna in result['snippet_highlighted_words']:                 
                        hsnip.append(sna)
                        asnip = []
                elif 'rich_snippet_list' in result:
                    for sn in result['rich_snippet_list']:
                        hsnip = []
                        asnip.append(sn)
                else:
                    hsnip = []
                    asnip = []
                    
                if 'snippet' in result:
                    snip = result['snippet']
                else:
                    snip = 'None' 
                
                payload = {'position': result['position'], 'query': query, 'snippet_highlighted_words': hsnip.copy(), 'rich_snippet_list': asnip.copy(), 'snippet': snip, 'link': result['link']}
                data.append(payload)
                hsnip.clear()
                asnip.clear()
                
        with open(f'{query}_google_data.csv', 'w') as file:
            
            # Create a CSV dictionary writer and add the student header as field names
            writer = csv.DictWriter(file, fieldnames=data_header)
            
            # Use writerows() not writerow()
            writer.writeheader()
            writer.writerows(data)
    
    except Exception as e:
         logger.error(f"Empty results | Message: {e}")
         pass
    
    finally:
        with open(f'{query}_google_data.csv', 'w', encoding="UTF8") as file:
            # Create a CSV dictionary writer and add the student header as field names
            writer = csv.DictWriter(file, fieldnames=data_header)
            # Use writerows() not writerow()
            writer.writeheader()
            writer.writerows(data)
            
import ast
import csv
import json
from serpapi import GoogleSearch
from config.settings import settings

logger = settings.logger
key = settings.serpApi_key4
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

    # search = GoogleSearch(params)
    # results = search.get_dict()

    get_highlighted_keywords(query)


def get_highlighted_keywords(query):
    global params, hsnip, asnip, snip, related_query_data, organic_data_header, question_data_header, related_query_data_header, organic_data, question_data
    
    snip = results_total = None
    hsnip = asnip = []
    organic_data = []
    question_data = []
    related_query_data = []
    organic_data_header = ['position','query', 'snippet_highlighted_words', 'rich_snippet_list', 'snippet', 'link']
    question_data_header = ['query', 'question', 'title', 'snippet', 'date', 'link']
    related_query_data_header = ['query', 'related']

    try:
        for page in range(0, 1000, 100):
            
            search = GoogleSearch(params)
             
            search.params_dict['start'] = page
            offset_results = search.get_dict()
            
            get_organic(query, offset_results)            
            get_questions(query, offset_results)                
            get_related_query(query, offset_results)
            
        if any(organic_data):    
            save2csv(f"{query}_organic", organic_data, organic_data_header)
        
        if any(question_data):    
            save2csv(f"{query}_question", question_data, question_data_header)
            
        if any(related_query_data):    
            save2csv(f"{query}_related_query", related_query_data, related_query_data_header)
    
    except Exception as e:
         logger.error(f"Empty results | Message: {e}")
         pass

def get_organic(query, offset_results):
    global hsnip, asnip, snip
    
    if 'organic_results' in offset_results:
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
            organic_data.append(payload)
            hsnip.clear()
            asnip.clear()

def get_related_query(query,  offset_results):
    
    if 'related_searches' in offset_results:
        for result in offset_results["related_searches"]:
            payload = {'query': query, 'related': result['query']}
                    
            related_query_data.append(payload)

def get_questions(query, offset_results):
    
    if 'related_questions' in offset_results:
        for result in offset_results["related_questions"]:
            date = snippet = None
            if 'date' in result:
                date = result['date']
            elif 'snippet' in result:
                snippet = result['snippet']
                    
            payload = {'query': query, 'question': result['question'], 'title': result['title'], 'snippet': snippet,'date': date, 'link': result['link']}
                    
            question_data.append(payload)

def save2csv(query, data, data_header):
        with open(f'data/{query}_google_data.csv', 'w', encoding="UTF8") as file:
                    # Create a CSV dictionary writer and add the student header as field names
            writer = csv.DictWriter(file, fieldnames=data_header)

                    # Use writerows() not writerow()
            writer.writeheader()
            writer.writerows(data)
            data.clear()
            
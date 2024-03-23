""" The code snippet you provided is a Python script that seems 
    to be part of a larger project involving web scraping using 
    the SerpApi library for Google search results."""

import csv
import os
from serpapi import GoogleSearch
from config.settings import settings


logger = settings.logger
KEY = settings.serpApi_key


def serp(query: str, country: str):

    organic_data = []
    question_data = []
    related_query_data = []
    organic_data_header = ['position', 'title', 'query',
                           'snippet_highlighted_words',
                           'rich_snippet_list', 'snippet',
                           'link']
    question_data_header = ['query', 'question',
                            'title', 'snippet',
                            'date', 'link']
    related_query_data_header = ['query', 'related']

    params = {
        "engine": "google",
        "q": query,
        "google_domain": "google.com",
        "lr": "lang_en|lang_ar",
        "filter": 0,
        "num": 20,
        "start": 0,
        "end": 1000,
        "location": "",
        "api_key": KEY,
    }

    if country:

        for item in settings.cities_dict[country]:

            location = GoogleSearch({}).get_location(item)
            if location:
                params['location'] = location[0]["canonical_name"]
            else:
                logger.error("City %s name incorrect", item)
                continue

            init_search = GoogleSearch(params)
            init_search.SERP_API_KEY = KEY
            pages = init_search.pagination()
            res = init_search.get_dict()

            if 'error' in res:

                logger.error("Request error | Message: %s", res['error'])

            else:

                for page in pages:
                
                    organic_data.append(get_organic(query, page))
                    question_data.append(get_questions(query, page))
                    related_query_data.append(get_related_query(query, page))

    else:

        init_search = GoogleSearch(params)
        pages = init_search.pagination()
        res = init_search.get_dict()

        if 'error' in res:

            logger.error("Request error | Message: %s", res['error'])

        else:

            for page in pages:

                organic_data.append(get_organic(query, page))
                question_data.append(get_questions(query, page))
                related_query_data.append(get_related_query(query, page))

    write_data(f"{query}_organic", organic_data, organic_data_header)
    write_data(f"{query}_question", question_data, question_data_header)
    write_data(f"{query}_related_query", related_query_data,
               related_query_data_header)


def write_data(name, data, data_header):
    """
    The function `write_data` saves flattened data to 
    a CSV file if the data is not empty.

    :param name: The `name` parameter is a string that 
    represents the name of the data file that will be
    saved
    :param data_header: The `data_header` parameter is 
    a list of column field names
    that correspond to the data being saved. It is used 
    to label the columns in the CSV file where the
    data will be written
    """

    if any(data):

        data = flatten_list(data)
        save2csv(f"{name}_data", data, data_header)


def flatten_list(data):
    """
    The `flatten_list` function takes a list of lists as input 
    and returns a flattened list containing all the elements 
    from the input lists.

    :param data: The `data` parameter in the `flatten_list` 
    function is a list of lists. Each inner list represents 
    a group of items that you want to flatten into a single 
    list. The function iterates over each inner list and 
    appends its elements to a temporary list, which is then 
    returned as a
    :return: The `flatten_list` function takes a list of 
    lists as input and returns a single list with
    all the elements from the input lists combined.
    """
    temp = []

    for qt in data:
        for qt_item in qt:
            temp.append(qt_item)

    return temp


def get_organic(query, offset_results):
    """
    The function `get_organic` extracts organic search results data from a given offset_results
    dictionary based on specified criteria.

    :param query: The function `get_organic` takes two parameters: `query` and `offset_results`. The
    `query` parameter is the search query for which you want to retrieve organic search results. The
    `offset_results` parameter is a dictionary containing search results, including organic results
    :param offset_results: The function `get_organic` takes two parameters: `query` and
    `offset_results`. The `offset_results` parameter is expected to be a dictionary containing
    information about search results, including organic results. The function then processes the organic
    results from the `offset_results` dictionary and extracts relevant information such
    :return: The function `get_organic(query, offset_results)` returns a list of dictionaries containing
    information about organic search results based on the input query and offset results. Each
    dictionary in the list includes the position of the result, the query used, the title of the result,
    highlighted words in the snippet, rich snippet information, the snippet itself, and the link to the
    result.
    """

    organic_data = []
    asnip = []
    hsnip = []

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

            title = None

            if 'title' in result:

                title = result['title']

            payload = {'position': result['position'], 'query': query, 'title': title, 'snippet_highlighted_words': hsnip.copy(
            ), 'rich_snippet_list': asnip.copy(), 'snippet': snip, 'link': result['link']}
            organic_data.append(payload)
            hsnip.clear()
            asnip.clear()

    return organic_data


def get_related_query(query,  offset_results):
    """
    The function `get_related_query` extracts related 
    search queries from the offset results and creates
    a payload with the original query and related query.

    :param query: The `query` parameter is the original 
    search query for which you want to find related
    searches. It is the input query for which you are 
    trying to retrieve related search queries
    :param offset_results: offset_results is a dictionary 
    containing search results, including related
    searches
    """

    related_query_data = []

    if 'related_searches' in offset_results:
        for result in offset_results["related_searches"]:
            payload = {'query': query, 'related': result['query']}

            related_query_data.append(payload)

    return related_query_data


def get_questions(query, offset_results):
    """
    The function `get_questions` extracts relevant information 
    from a list of related questions and stores it in a payload 
    dictionary.

    :param query: The `query` parameter is the search query for 
    which you want to retrieve related questions
    :param offset_results: offset_results is a dictionary containing 
    information about related questions. It may have keys like 
    "related_questions" which holds a list of related questions with
    details such as question, title, snippet, date, and link
    """

    question_data = []

    if 'related_questions' in offset_results:
        for result in offset_results["related_questions"]:

            date = snippet = None

            if 'date' in result:

                date = result['date']

            elif 'snippet' in result:

                snippet = result['snippet']

            payload = {'query': query, 'question': result['question'], 'title': result['title'],
                       'snippet': snippet, 'date': date, 'link': result['link']}

            question_data.append(payload)

    return question_data


def save2csv(query, data, data_header):
    """
    The function `save2csv` saves data to a CSV file 
    with a specified query name and clears the data
    after writing.

    :param query: The `query` parameter is a string that 
    represents the name or identifier of the data
    being saved to the CSV file. It is used to generate 
    the filename for the CSV file where the data will be saved
    :param data: The `data` parameter in the `save2csv` function 
    is typically a list of dictionaries where each dictionary 
    represents a row of data to be written to the CSV file. Each 
    dictionary should have keys that correspond to the field names 
    specified in the `data_header` parameter   
    :param data_header: The `data_header` parameter is a list of 
    strings that represent the column headers for the CSV file that 
    will be created. Each string in the list corresponds to a column in
    the CSV file
    """
    with open(f'data/{query}_google_data.csv', 'w', newline='', encoding="utf-8-sig") as file:

        writer = csv.DictWriter(file, fieldnames=data_header)

        writer.writeheader()
        writer.writerows(data)

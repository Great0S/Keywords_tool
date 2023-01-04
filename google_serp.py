from serpapi import GoogleSearch
from config.settings import settings

logger = settings.logger
key = settings.serpApi_key5

def serp(query: str, lang: str):

    params = {
        "engine": "google",
        "q": query,
        "google_domain": "google.com",
        "gl": "us",
        "hl": lang,
        "api_key": key,
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    for result in results["suggestions"]:
        logger.info(result['value'])
from serpapi import GoogleSearch
from config.settings import settings

logger = settings.logger
key = settings.serpApi_key5


def autocomplete(query):
    params = {
        "engine": "google_autocomplete",
        "q": query,
        "api_key": key,
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    for result in results["suggestions"]:
        logger.info(result['value'])

from serpapi import GoogleSearch
from config.settings import settings

logger = settings.logger
key = settings.serpApi_key5


def related(next_token):
    params = {
        "engine": "google_related_questions",
        "next_page_token": next_token,
        "api_key": key
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    logger.info(results)

import os
import time
from rich.prompt import Prompt

from config.settings import settings
from modules.google_serp import serp

logger = settings.logger


def queries_handler(query: str, lang: str):
    """
    The function `queries_handler` logs the start of scraping, records the start time, calls the `serp`
    function with the provided query and language, and then logs the time taken for scraping to
    complete.
    
    :param query: The `query` parameter in the `queries_handler` function is a string that represents
    the search query or term that will be used for scraping search engine results
    :type query: str
    :param lang: The `lang` parameter in the `queries_handler` function is used to specify the language
    in which the search query should be performed. It is likely used to customize the search results
    based on the specified language
    :type lang: str
    """

    logger.info("Scraping start")   
    start_time = time.time() 
    serp(query, lang)
    logger.info(f"Scraped in {(time.time() - start_time):.2f} seconds")


# clearing the console from unnecessary
def cls():
    """
    The function `cls()` is used in Python to clear the console screen.
    :return: The `os.system("cls")` function is being returned.
    """
    return os.system("cls")


cls()


logger.info("SerpApi Keywords research")

query = Prompt.ask("Query")
lang = Prompt.ask("Language ISO-Code")

queries_handler(query, lang)
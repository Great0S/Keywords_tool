import getopt
import os
import time
from rich.prompt import Prompt

from config.settings import settings
from modules.google_serp import serp

logger = settings.logger


def queries_handler(query: str, lang: str):
    
    logger.info("Scraping start")   
    start_time = time.time() 
    serp(query, lang)
    logger.info(f"Scraped in {(time.time() - start_time):.2f} seconds")


# clearing the console from unnecessary
def cls(): return os.system("cls")


cls()


logger.info("SerpApi Keywords research")

query = Prompt.ask("Query")
lang = Prompt.ask("Language ISO-Code")

queries_handler(query, lang)
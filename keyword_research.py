import getopt
import os
import sys

from config.settings import settings
# from modules.google_autocomplete import autocomplete
from modules.google_questions import question
# from modules.google_related_question import related
from modules.google_serp import serp

logger = settings.logger


def queries_handler(query: str, lang: str):
    
    logger.info("Serp results")
    serp(query, lang)
    
    # logger.info("Autocomplete results")
    # autocomplete(query)
    
    logger.info("Question results")
    question(query)
    
    # logger.info("Related results")
    # related(query)


# clearing the console from unnecessary
def cls(): return os.system("cls")


cls()


logger.info("Keywords research starts")

logger.info("Query: ")
query = input()
logger.info("Language ISO-Code: ")
lang = input()

queries_handler(query, lang)
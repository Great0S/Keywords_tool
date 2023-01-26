from logging import config as Config
import logging
from deep_translator import GoogleTranslator
from pydantic import BaseSettings
from config.logger import log_config

# Declaring global variables
class Settings(BaseSettings):
    
    # Logger config
    Config.dictConfig(log_config)
    logger = logging.getLogger('mainLog')
    logs_dir: str = 'logs/'
    
    # Google serpApi keys
    serpApi_key: str = ''   
    
    class Config:
        case_sensitive = True

settings = Settings()
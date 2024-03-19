"""The code snippet you provided is importing necessary
 modules and classes for setting up
 configuration settings in a Python application."""

# Here is a breakdown of each import statement:
from logging import config
import logging
from pydantic_settings import BaseSettings
from config.logger import log_config

# Declaring global variables


class Settings(BaseSettings):

    """The class `Settings` defines configuration settings 
    including logger configuration, directory for
    logs, Google serpApi key, and case sensitivity."""

    # Logger config
    config.dictConfig(log_config)
    logger = logging.getLogger('mainLog')
    logs_dir: str = 'logs/'

    # Google serpApi keys
    serpApi_key: str = ''

    class Config:
        case_sensitive = True


settings = Settings()

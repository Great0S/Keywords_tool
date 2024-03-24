"""The code snippet you provided is importing necessary
 modules and classes for setting up
 configuration settings in a Python application."""

# Here is a breakdown of each import statement:
from logging import Logger, config
import logging
import os
from typing import ClassVar
from pydantic_settings import BaseSettings
from config.logger import log_config


# Declaring global variables
class Settings(BaseSettings):

    """The class `Settings` defines configuration settings 
    including logger configuration, directory for
    logs, Google serpApi key, and case sensitivity."""

    # Logger config
    config.dictConfig(log_config)
    logger: ClassVar[Logger] = logging.getLogger('mainLog')
    logs_dir: str = 'logs/'

    # Google serpApi keys
    serpApi_key: str = f"{os.getenv('APIKEY2')}"

    # Locations
    cities_dict: dict = {
        "saudi arabia": [
            "Riyadh", "Jeddah", "Mecca", "Medina", "Dammam", "Khobar", "Taif", "Tabuk",
            "Buraydah", "Khamis Mushait", "Hail", "Najran", "Al-Qatif", "Yanbu", "Al Hofuf",
            "Jubail", "Abha", "Jizan", "Al-Kharj", "Hafar Al-Batin"
        ],
        "usa": [
            "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia",
            "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville",
            "San Francisco", "Columbus", "Fort Worth", "Indianapolis", "Charlotte",
            "Seattle", "Denver", "Washington"
        ],
        "uae": [
            "Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Ras Al Khaimah", "Fujairah",
            "Umm Al Quwain"
        ],
        "qatar": [
            "Doha", "Al Rayyan", "Umm Salal", "Al Wakrah", "Al Khor", "Al Shamal", "Mesaieed"
        ]
    }

    class Config:
        """The `Config` class in Python has a `case_sensitive` attribute set to `True`."""
        case_sensitive = True


settings = Settings()

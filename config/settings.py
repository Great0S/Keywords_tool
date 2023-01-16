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
    
    # Translation
    turk_translate = GoogleTranslator(source='tr', target='en')
    english_translate = GoogleTranslator(source='en', target='ar')
    arabic_translate = GoogleTranslator(source='ar', target='en')

    # Telegram API Config
    api_id: int = 7148663
    api_hash: str = '81c16de88cd5e25fcbf01e5af332b41f'

    # Telegram BOT info
    username: str = 'albeyanfashion2'
    phone: int = 905434050709
    token: str = '5754073767:AAE3IbbE7-zXKGMg1fqunFxsUOg5K-kH6GI'
    channel_id: str = '@BeyanStorebot'
    session_name: str = 'tele_bot'

    # Telegram Channels info
    women_ids = [-1001411372097, -1001188747858, -1001147535835, -1001237631051, -1001653408221]

    # Ecwid info    
    category_id: int = 127443592

    # Ecwid connection info
    products_url = "https://app.ecwid.com/api/v3/63690252/products"
    category_url = "https://app.ecwid.com/api/v3/63690252/categories"
    ecwid_token = "?token=secret_4i936SRqRp3317MZ51Aa4tVjeUVyGwW7"
    payload = {}
    ecwid_headers = {
    "Authorization": "Bearer secret_4i936SRqRp3317MZ51Aa4tVjeUVyGwW7",
    "Content-Type": 'application/json;charset: utf-8'
    }

    # Google serpApi keys
    serpApi_key1: str = 'e2f1eb7309c17ffc3443c9780ce1c250daf898f28fa1658ebd7c74556b629bfd'
    serpApi_key2: str = '2ee39e4a62c53b8925eedda4e64b3e0f3eed31d1d15cad2cc810a34d073c37f6'
    serpApi_key3: str = '9079dcad0cf0a9f24fe95b8a53579fd9140d600861ea10151be0b237867a07ff'
    serpApi_key4: str = '477698bdf2954936a202befb298d84c929860ccd2e18b4ea5bf994bfda3718d6'
    serpApi_key5: str = 'ea129d0e45632d59617087eacf26bf48e3ce39458e0bb086c5513df96c413717'
    serpApi_key6: str = '78a0e56f4d74e7e3acef3bce9bd0c116fe7999802aac437af911bf45d7898ea6'
    serpApi_key7: str = '5b9c4228022e9cce8d288d0af14004cce63957b5922e2335b410631025d686b6'
    serpApi_key8: str = '3aaff53cc10bdbc386caf955be287b334daee40d4c85702b35b034c1a17f10a1'
    serpApi_key9: str = '2c76a8db8a76842ddb94e6fdf754aa85c1682b7bdc52b38c77c637dc4d03352b'
    serpApi_key10: str = '4435d3a85dec7cb053ae29a3e360d111ae85170fa24d8e108c702d3c9b56374c'
    
    
    class Config:
        case_sensitive = True

settings = Settings()
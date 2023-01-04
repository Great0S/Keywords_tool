import os 
from serpapi import GoogleSearch

params = {
  "engine": "google_autocomplete",
  "q": "minecraft",
  "api_key": '2ee39e4a62c53b8925eedda4e64b3e0f3eed31d1d15cad2cc810a34d073c37f6', # environment variable 
}

search = GoogleSearch(params)
results = search.get_dict()

for result in results["suggestions"]:
  print(result['value'])
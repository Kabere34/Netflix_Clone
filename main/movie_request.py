import json
import requests
from netflix import settings

apikey=settings.API_KEY
movieurl=settings.MOVIE_URL



def api_results(category):
  requests_url=movieurl.format(category,apikey)
  response=requests.get(requests_url)
  data=response.text
  api_dictionary=json.loads(data)
  print(api_dictionary)
  return api_dictionary.get('results')

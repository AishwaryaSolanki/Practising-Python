import requests
import json

SUBSCRIPTION_KEY = '9ada26d462ff4c2d890df1152836b753'
ADDRESS = 'https://westus.api.cognitive.microsoft.com/vision/v2.1/' + 'analyze'
PARAMS = { 'visualFeatures' : 'Description,Color',
           'language' : 'en' }
IMG_PATH = '../bear.png'
IMG_DATA = open(IMG_PATH, 'rb').read()

HEADERS = { 'Content-Type' : 'application/octet-stream',
            'Ocp-Apim-Subscription-Key' : SUBSCRIPTION_KEY}

RESPONSE = requests.post(ADDRESS,
                        headers=HEADERS,
                        params=PARAMS,
                        data=IMG_DATA)

RESPONSE.raise_for_status()

RESULT = RESPONSE.json()
print(json.dumps(RESULT))

import requests

import json


res = requests.post('https://api.short.io/links', {
      'domain': '439z.short.gy',
      'originalURL': 'https://www.google.com/search?channel=fs&client=ubuntu&q=how+to+use+short.io',
}, headers = {
      'authorization': 'sk_DDAGhbmUt6j7NaiB',
      'content-type': 'application/json'
}, json=True)

# res.raise_for_status()
data = res.json()

print(data)
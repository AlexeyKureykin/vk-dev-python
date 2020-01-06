import requests
import json
import time

f = open('token.txt', 'r')
token = f.read()
f.close()

params = {
    'v':'5.52',
    'access_token': token,
    'owner_id': 382533516,
    'message' : 1,
    'attachments': 'photo382533516_457240293'
}
r = requests.get('https://api.vk.com/method/wall.post?', params=params)
j = json.loads(r.content)
print(j)
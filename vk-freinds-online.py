import requests
import json

f = open('token.txt', 'r')
token = f.read()
f.close()

params = {'v':'5.52', 'access_token':token}
r = requests.get('https://api.vk.com/method/friends.getOnline?', params=params)
friends = json.loads(r.content)

i = friends['response']
online = len(i)

print('Всего друзей онлайн:', online)
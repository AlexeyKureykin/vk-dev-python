import requests
import json
import time

f = open('e:\token.txt', 'r')
token = f.read()
f.close()

#Получить список id своих друзей
params = {'v':'5.52', 'access_token':token}
r = requests.get('https://api.vk.com/method/friends.get?', params=params)
friends = json.loads(r.content)

max_count = 0
max_user_id = 0

for friend in friends['response']['items']:
    params = {'user_id' : friend, 'v' : '5.52', 'access_token':token}
    r = requests.get('https://api.vk.com/method/friends.get?', params=params)
    f = json.loads(r.content)
    count = f['response']['count']  #Получить число друзей у друга
    if count > max_count:
        max_count = count
        max_user_id = friend
    
    time.sleep(0.1)
print(max_user_id, max_count)

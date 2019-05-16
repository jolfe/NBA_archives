import requests
import json

request_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'stats.nba.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

team = '1610612742'

url = "https://stats.nba.com/stats/commonteamroster/?Season=1999-00&TeamID=" + team

response = requests.get(url, headers = request_headers)

data = response.json()

print (response)

class Player():
    def __init__(self, name, position, height, weight):
        self.name = name
        self.position = position
        self.height = height
        self.weight = weight

objs = []

def run():
    x = 0;
    players = []

    for i in data['resultSets'][0]['rowSet']:
        name = data['resultSets'][0]['rowSet'][x][3]
        position = data['resultSets'][0]['rowSet'][x][5]
        height = data['resultSets'][0]['rowSet'][x][6]
        weight = data['resultSets'][0]['rowSet'][x][7]
        stats = 'Name: ' + name + ' Position: ' + position + ' Height: ' + height + ' Weight: ' + weight
        objs.append(Player(name, position, height, weight))
        x+=1

    return (players)
val = 0
list = run()
data2 = {}
for x in objs:
    data2[val] = x.name + ", " + x.position + ", " + x.height + ", " +x.weight;
    val+=1
    json_data = json.dumps(data2)

with open('data.json', 'w') as outfile:
     json.dump(json_data + "test", outfile)
print (json_data)

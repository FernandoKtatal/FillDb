import requests
import json

######################### nuuvem data #######################
with open('../Crawler/tutorial/nuuvem.json', 'r') as jsonfile:
	json_content = json.load(jsonfile)

for json_item in json_content:
    key = json_item['name']
    test = {'official': key}
    price = json_item['price'].replace(',','.')

    r = requests.get('http://localhost:8000/api/v1/games/', params=test)
    data = r.json().get('results')

    if (len(data) == 0):
        r = requests.post('http://localhost:8000/api/v1/games/', data={'official': json_item['name'],'name': json_item['name'], 'price': float(price), 'link' : json_item['link'], 'img': json_item['img']} )
        print("nuuvem game added")
    for item in data:
        if(len(data) != 0):
            nuuvemID = item['id']
            r = requests.put('http://localhost:8000/api/v1/games/'+ str(nuuvemID) + '/',data={'name': json_item['name'], 'price': float(price), 'link' : json_item['link'], 'img': json_item['img']} )
            print("NEW PRICE WITH nuuvem")


######################### steam data #######################
with open('../Crawler/tutorial/steam.json', 'r') as jsonfile:
    json_content = json.load(jsonfile)

for json_item in json_content:
    key = json_item['nameSteam']
    test = {'official': key}
    price = json_item['priceSteam'].replace('R$','').replace('.','').replace(',','.')

    r = requests.get('http://localhost:8000/api/v1/games/', params=test)
    data = r.json().get('results')
    if (len(data) == 0):
        r = requests.post('http://localhost:8000/api/v1/games/', data={'official': json_item['nameSteam'],'nameSteam': json_item['nameSteam'],  'priceSteam': float(price), 'linkSteam': json_item['linkSteam'], 'imgSteam': json_item['imgSteam']})
        print("steam game added")
# for each item found print the name
    for item in data:
        if (len(data) != 0):
            steamID = item['id']
            r = requests.put('http://localhost:8000/api/v1/games/'+ str(steamID) + '/', data={'nameSteam': json_item['nameSteam'], 'priceSteam': float(price), 'linkSteam': json_item['linkSteam'], 'imgSteam': json_item['imgSteam']})
            print("NEW PRICE WITH STEAM")


######################### G2a data #######################
with open('../Crawler/tutorial/g2a.json', 'r') as jsonfile:
	json_content = json.load(jsonfile)

for json_item in json_content:
    key = json_item['nameG2a']
    test = {'official': key}
    price = json_item['priceG2a']

    r = requests.get('http://localhost:8000/api/v1/games/', params=test)
    data = r.json().get('results')

    if (len(data) == 0):
        r = requests.post('http://localhost:8000/api/v1/games/', data={'official': json_item['nameG2a'],'nameG2a': json_item['nameG2a'], 'priceG2a': float(price), 'linkG2a' : json_item['linkG2a'], 'imgG2a': json_item['imgG2a']} )
        print("G2a game added")

    for item in data:
        if(len(data) != 0):
            nuuvemID = item['id']
            r = requests.put('http://localhost:8000/api/v1/games/'+ str(nuuvemID) + '/',data={'nameG2a': json_item['nameG2a'], 'priceG2a': float(price), 'linkG2a' : json_item['linkG2a'], 'imgG2a': json_item['imgG2a']} )
            print("NEW PRICE WITH G2a")

import requests
import json

######################### nuuvem data #######################
with open('../Crawler/tutorial/nuuvem.json', 'r') as jsonfile:
	json_content = json.load(jsonfile)

for json_item in json_content:
    key = json_item['nameNu']
    test = {'official': key}
    price = json_item['priceNu'].replace(',','.')

    r = requests.get('http://localhost:8000/api/v1/games/', params=test)
    data = r.json().get('results')

    if (len(data) == 0):
        r = requests.post('http://localhost:8000/api/v1/games/', data={'official': json_item['nameNu'],'name': json_item['nameNu'], 'priceNu': float(price), 'linkNu' : json_item['linkNu'], 'img': json_item['imgNu']} )
        print("nuuvem game added")
    for item in data:
        if(len(data) != 0):
            nuuvemID = item['id']
            r = requests.put('http://localhost:8000/api/v1/games/'+ str(nuuvemID) + '/',data={'priceNu': float(price), 'linkNu' : json_item['linkNu']})
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
        r = requests.post('http://localhost:8000/api/v1/games/', data={'official': json_item['nameSteam'],'name': json_item['nameSteam'], 'priceSteam': float(price), 'linkSteam': json_item['linkSteam'], 'img': json_item['imgSteam']})
        print("steam game added")

    for item in data:
        if (len(data) != 0):
            steamID = item['id']
            r = requests.put('http://localhost:8000/api/v1/games/'+ str(steamID) + '/', data={'priceSteam': float(price), 'linkSteam': json_item['linkSteam']})
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
        r = requests.post('http://localhost:8000/api/v1/games/', data={'official': json_item['nameG2a'],'name': json_item['nameG2a'], 'priceG2a': float(price), 'linkG2a' : json_item['linkG2a'], 'img': json_item['imgG2a']} )
        print("G2a game added")

    for item in data:
        if(len(data) != 0):
            G2aID = item['id']
            r = requests.put('http://localhost:8000/api/v1/games/'+ str(G2aID) + '/',data={'priceG2a': float(price), 'linkG2a' : json_item['linkG2a']} )
            print("NEW PRICE WITH G2a")

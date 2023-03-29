import requests
import json
def get_kanjis():
    kanjis = []
    url = "http://localhost:8765"
    find_cards = {
    "action": "findCards", 
    "version": 6,
    "params": {
        "query": "\"deck:Kanji::1.Recognition Cards\" -is:new"
        }
    }
    cards_info = {
    "action": "cardsInfo", 
    "version": 6,
    "params": {
        "cards": []
        }
    }
    response = requests.post(url, json=find_cards)
    response_json = response.json()
    cards_info = {
    "action": "cardsInfo", 
    "version": 6,
    "params": {
        "cards": []
        }
    }
    cards_info["params"]["cards"] = response_json["result"]
    info = requests.post(url, json=cards_info)
    info_d = info.json()
    for count, value in enumerate(info_d["result"]):
        kanjis.append(value["fields"]["Kanji"]["value"])
    return kanjis

def joyou_to_dict():
    contents = ""
    all_kanjis = []
    with open('joyou.txt') as f:
        contents = f.read()
    for count,value in enumerate(contents):
        all_kanjis.append(value)
    return all_kanjis
        
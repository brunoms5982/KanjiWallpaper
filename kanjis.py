import requests
import json
def get_learn_kanjis():
    #Getting Learning Kanjis
    learn_kanjis = []
    url = "http://localhost:8765"
    find_learn_cards = {"action": "findCards", "version": 6,"params": {"query": "\"deck:Kanji::1.Recognition Cards\" is:learn"}}
    response = requests.post(url, json=find_learn_cards)
    response_json = response.json()
    cards_info = {"action": "cardsInfo", "version": 6,"params": {"cards": []}}
    cards_info["params"]["cards"] = response_json["result"]
    info = requests.post(url, json=cards_info)
    info_d = info.json()
    for count, value in enumerate(info_d["result"]):
        learn_kanjis.append(value["fields"]["Kanji"]["value"])
    return learn_kanjis
def get_review_kanjis():
    review_kanjis = []
    interval = []
    url = "http://localhost:8765"
    find_review_cards = {"action": "findCards", "version": 6,"params": {"query": "\"deck:Kanji::1.Recognition Cards\" is:review"}}
    response = requests.post(url, json=find_review_cards)
    response_json = response.json()
    cards_info = {"action": "cardsInfo", "version": 6,"params": {"cards": []}}
    cards_info["params"]["cards"] = response_json["result"]
    info = requests.post(url, json=cards_info)
    info_d = info.json()
    for count, value in enumerate(info_d["result"]):
        review_kanjis.append(value["fields"]["Kanji"]["value"])
        interval.append(value["interval"])
    review_dict = dict(zip(review_kanjis,interval))
    return review_dict
#def classify_review_kanjis():
    
    











def joyou_to_dict():
    contents = ""
    all_kanjis = []
    with open('joyou.txt') as f:
        contents = f.read()
    for count,value in enumerate(contents):
        all_kanjis.append(value)
    return all_kanjis
        
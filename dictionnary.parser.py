import json
import os

def save(data):
    with open("word.data.json", "w", encoding="utf-8") as f:
        json.dump(data, f)

def load():
    with open("word.data.json", "r", encoding="utf-8") as f:
        return json.load(f)

DCT="dico.en.txt"
DATA=load()
DATA.update(start={"count":0})
for line in open(DCT,"r",encoding="utf-8").read().splitlines():
    i=0
    DATA=load()
    if not line[0] in DATA["start"].keys():
        DATA["start"].update({line[0]:0})
    DATA["start"][line[0]]+=1
    DATA["start"]["count"]+=1
    for ch in line:
        if not ch in DATA.keys():
            DATA.update(ch={"count":0})
            if not line[i+1] in DATA[ch].keys():
                DATA[ch].update({line[i+1]:0})
        DATA[ch]["count"]+=1
        DATA[ch][line[i+1]]+=1
        i+=1
        save()

import json
import os

def save(data):
    with open("word.data.json", "w", encoding="utf-8") as f:
        json.dump(data, f)
def load():
    with open("word.data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def KeyErrorHandler(key,data):
    try:
        data[key]
        return False
    except KeyError:
        return True
save({"en":{}})
n=0
LANGUAGE="en"
DCT="dico.en.txt"
print(load())
DATA=load()
DATA[LANGUAGE].update(start={"count":0})
save(DATA)
l=0
for line in open(DCT,"r",encoding="utf-8").read()[1:].splitlines():
    i=0
    DATA=load()
    if KeyErrorHandler(line[0],DATA[LANGUAGE]["start"]):
        DATA[LANGUAGE]["start"].update({line[0]:0})
    DATA[LANGUAGE]["start"][line[0]]+=1
    DATA[LANGUAGE]["start"]["count"]+=1
    l+=1
    for ch in line:
        if KeyErrorHandler(ch,DATA[LANGUAGE]):
            DATA[LANGUAGE].update({ch:{"count":0}})
        if i>=len(line)-1:
            DATA[LANGUAGE][ch]["count"]+=1
            if KeyErrorHandler("end",DATA[LANGUAGE][ch]):
                DATA[LANGUAGE][ch].update(end=0)
            DATA[LANGUAGE][ch]["end"]+=1
            i+=1
            continue
        if KeyErrorHandler(line[i+1],DATA[LANGUAGE][ch]):
            DATA[LANGUAGE][ch].update({line[i+1]:0})
        DATA[LANGUAGE][ch]["count"]+=1
        DATA[LANGUAGE][ch][line[i+1]]+=1
        i+=1
    
    save(DATA)
print(load())

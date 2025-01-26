import json
import os
import time

class Parser:
    def __init__(self,language="words_alpha",data={},DICT="words_alpha.txt"):
        self.LANGUAGE=language
        self.DATA=data
        self.DICT=DICT
        self.STATS={"total":0}
    def statsUpdate(self,ch):
        if not ch in self.STATS.keys():
            self.STATS.update({ch:[0,0]})
        self.STATS[ch][0]+=1
        self.STATS["total"]+=1
    def getData(self):
        return self.DATA[self.LANGUAGE]
    def save(self,data=None):
        if data==None:
            data=self.DATA
        with open("word.data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
    def load(self):
        with open("word.data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    def loadData(self):
        self.DATA=self.load()
    def reload(self,data=None):
        if data==None:
            data=self.DATA
        self.save(data)
        self.loadData()
    def KeyErrorHandler(self,key,data):
        try:
            data[key]
            return False
        except KeyError:
            return True


parser=Parser()
print(" |=========================| ")
print(" |     Dict generator      | ")
print(" |-------------------------| ")
print(" | Enter file              | ")
print(" |=========================| ")
inp=input(">>> ")
parser.DICT="dico.en.txt" if inp=="" else inp
print(" |=========================| ")
print(" |     Dict generator      | ")
print(" |-------------------------| ")
print(" | Enter language          | ")
print(" |=========================| ")
inp=input(">>> ")
parser.LANGUAGE=parser.DICT if inp == "" else inp
print(" |=========================| ")
print(" |     Word generator      | ")
print(" |-------------------------| ")
print(" | Del chars and counts ?  | ")
print(" | 0 : Yes                 | ")
print(" | 1 : No                  | ")
print(" |=========================| ")
inp=input(">>> ")
remove_chars_and_counts = 0 if inp=="" else int(inp)
if parser.KeyErrorHandler(parser.LANGUAGE,parser.DATA):
    parser.loadData()
    parser.DATA.update({parser.LANGUAGE:{}})
    parser.save()
n=0
print("Counting chars...")
parser.reload(parser.getData().update({"counts":{"start":0},"chars":{"start":{}}}))
l=0
file=open(parser.DICT,"r",encoding="utf-8").read()
if file[0]=='\ufeff':
    file=file[1:]
for line in file.splitlines():
    i=0
    parser.statsUpdate(line[0])
    if parser.KeyErrorHandler(line[0],parser.getData()["chars"]["start"]):
        parser.getData()["chars"]["start"].update({line[0]:0})
    parser.getData()["chars"]["start"][line[0]]+=1
    parser.getData()["counts"]["start"]+=1
    l+=1
    for ch in line:
        parser.statsUpdate(ch)
        if parser.KeyErrorHandler(ch,parser.getData()["chars"]):
            parser.getData()["chars"].update({ch:{}})
            parser.getData()["counts"].update({ch:0})
        if i>=len(line)-1:
            parser.getData()["counts"][ch]+=1
            if parser.KeyErrorHandler("end",parser.getData()["chars"][ch]):
                parser.getData()["chars"][ch].update(end=0)
            parser.getData()["chars"][ch]["end"]+=1
            i+=1
            continue
        if parser.KeyErrorHandler(line[i+1],parser.getData()["chars"][ch]):
            parser.getData()["chars"][ch].update({line[i+1]:0})
        parser.getData()["counts"][ch]+=1
        parser.getData()["chars"][ch][line[i+1]]+=1
        i+=1
print("Done")
print(f"Scaned lines : {l}")

parser.reload()

print("Weights...")
parser.getData().update(weights={})
d=0
for keys in parser.getData()["chars"].keys():
    i=0
    if parser.KeyErrorHandler(keys,parser.getData()["weights"]):
        parser.getData()["weights"].update({keys:{}})
    for key in parser.getData()["chars"][keys].keys():
        if parser.KeyErrorHandler(key,parser.getData()["weights"][keys]):
            parser.getData()["weights"][keys].update({key:{}})
        parser.getData()["weights"][keys][key]=float(parser.getData()["chars"][keys][key]/parser.getData()["counts"][keys])
        i+=1
if not remove_chars_and_counts:
    del parser.getData()["chars"]
    del parser.getData()["counts"]
    print("Chars and counts successfully removed")
print("Done")
for i in parser.STATS.keys():
    if i=="total":continue
    parser.STATS[i][1]=(parser.STATS[i][0]/parser.STATS["total"])*100
print("| Stats :","V"*19)
for i in parser.STATS.keys():
    print("|",i,":",parser.STATS[i])
parser.save()

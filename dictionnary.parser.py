import json
import os

class Parser:
    def __init__(self,language="en",data={},DICT="dico.en.txt"):
        self.LANGUAGE=language
        self.DATA=data
        self.DICT=DICT
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
        self.save(data)
        self.loadData()
    def KeyErrorHandler(self,key,data):
        try:
            data[key]
            return False
        except KeyError:
            return True


parser=Parser()
parser.reload({"en":{}})
n=0
print(parser.DATA)
parser.reload(parser.getData().update(start={"count":0}))
l=0
file=open(parser.DICT,"r",encoding="utf-8").read()
if file[0]=='\ufeff':
    file=file[1:]
for line in file.splitlines():
    i=0
    parser.reload()
    if parser.KeyErrorHandler(line[0],parser.getData()["start"]):
        parser.getData()["start"].update({line[0]:0})
    parser.getData()["start"][line[0]]+=1
    parser.getData()["start"]["count"]+=1
    l+=1
    for ch in line:
        if parser.KeyErrorHandler(ch,parser.getData()):
            parser.getData().update({ch:{"count":0}})
        if i>=len(line)-1:
            parser.getData()[ch]["count"]+=1
            if parser.KeyErrorHandler("end",parser.getData()[ch]):
                parser.getData()[ch].update(end=0)
            parser.getData()[ch]["end"]+=1
            i+=1
            continue
        if parser.KeyErrorHandler(line[i+1],parser.getData()[ch]):
            parser.getData()[ch].update({line[i+1]:0})
        parser.getData()[ch]["count"]+=1
        parser.getData()[ch][line[i+1]]+=1
        i+=1

parser.reload()

print(parser.DATA)

import json
import random

class Compiler:
    def __init__(self,language:str="en",data:dict={},currentchar:str=""):
        self.LANGUAGE=language
        self.DATA=data
        self.CurrentChar=currentchar
        self.Output=""
    def getChar(self):
        return self.CurrentChar
    def getData(self):
        return self.DATA[self.LANGUAGE]["weights"]
    def load(self):
        with open("word.data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    def loadData(self):
        self.DATA=self.load()
    def loadValues(self):
        return list(self.DATA[self.LANGUAGE]["weights"][self.CurrentChar].values())
    def loadKeys(self):
        return list(self.DATA[self.LANGUAGE]["weights"][self.CurrentChar].keys())



compiler=Compiler(currentchar="start")
compiler.loadData()

compiler.CurrentChar="start"
while True:
    if compiler.CurrentChar=="end":
        break
    
    compiler.CurrentChar=''.join(random.choices(compiler.loadKeys(),weights=compiler.loadValues()))
    if compiler.CurrentChar=="end":
        break
    compiler.Output+=compiler.CurrentChar
    

print(compiler.Output)

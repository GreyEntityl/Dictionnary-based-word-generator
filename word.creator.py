import json
import random

class Compiler:
    def __init__(self,language:str="en",data:dict={},currentchar:str="",withcustomlength:bool=False):
        self.LANGUAGE=language
        self.DATA=data
        self.CurrentChar=currentchar
        self.Output=""
        self.withCustomLength=withcustomlength
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

def main():
    print(" |=========================| ")
    print(" |     Word generator      | ")
    print(" |-------------------------| ")
    print(" | 0 : Undetermined length | ")
    print(" | 1 : Determined length   | ")
    print(" |=========================| ")
    compiler=Compiler(currentchar="start",withcustomlength=int(input(">>> ")))
    compiler.loadData()
    
    length=0
    if compiler.withCustomLength:
        print(" | Type the length of your(s) world | ")
        length=int(input(">>> "))
    print(" |=========================| ")
    print(" |     Word generator      | ")
    print(" |-------------------------| ")
    print(" | Number of words         | ")
    print(" |=========================| ")
    d=int(input(">>>"))
    i=0
    while i<=d:
        compiler.Output=""
        compiler.CurrentChar="start"
        while length>len(compiler.Output) or (not compiler.withCustomLength):
            if compiler.withCustomLength and "end" in compiler.DATA[compiler.LANGUAGE]["weights"][compiler.CurrentChar].keys():
                print(compiler.DATA[compiler.LANGUAGE]["weights"][compiler.CurrentChar]["end"])
                del compiler.DATA[compiler.LANGUAGE]["weights"][compiler.CurrentChar]["end"]
            char=''.join(random.choices(compiler.loadKeys(),weights=compiler.loadValues()))
            if char=="end":
                break
            compiler.CurrentChar=char
            compiler.Output+=compiler.CurrentChar
    

        print(compiler.Output)
        i+=1
if __name__=="__main__":
    main()
    

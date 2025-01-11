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
        return self.DATA[self.LANGUAGE]["weights"] #Get wieghts of a language
    def load(self):
        with open("word.data.json", "r", encoding="utf-8") as f: #Load the json file
            return json.load(f)
    def loadData(self):
        self.DATA=self.load()
    def loadValues(self):
        return list(self.DATA[self.LANGUAGE]["weights"][self.CurrentChar].values()) #Get the weights values of the chars could be after the char
    def loadKeys(self):
        return list(self.DATA[self.LANGUAGE]["weights"][self.CurrentChar].keys()) #Get the weights of the chars could be after the char

def main():
    print(" |=========================| ")
    print(" |     Word generator      | ")
    print(" |-------------------------| ")
    print(" | Output file             | ")
    print(" |=========================| ")
    OUTPUT_FILE=input(">>> ")
    withoutput_file=True
    if OUTPUT_FILE=="":
        withoutput_file=False
    print(" |=========================| ")
    print(" |     Word generator      | ")
    print(" |-------------------------| ")
    print(" | Enter language          | ")
    print(" |=========================| ")
    LANG=input(">>> ")
    print(" |=========================| ")
    print(" |     Word generator      | ")
    print(" |-------------------------| ")
    print(" | 0 : Undetermined length | ")
    print(" | 1 : Determined length   | ")
    print(" |=========================| ")
    inp=input(">>> ")
    compiler=Compiler(currentchar="start",language="en" if LANG=="" else LANG,withcustomlength=0 if inp=="" else int(inp))
    compiler.loadData()
    
    length=0
    if compiler.withCustomLength:
        print(" | Type the length of your words | ")
        inp=input(">>> ")
        length=10 if inp=="" else int(inp)
    print(" |=========================| ")
    print(" |     Word generator      | ")
    print(" |-------------------------| ")
    print(" | Number of words         | ")
    print(" |=========================| ")
    inp=input(">>> ")
    d=100 if inp=="" else int(inp)
    i=0
    print(" |=========================>>> ")
    print(" |     Word generator      >>> ")
    print(" |------------------------->>> ")
    if withoutput_file:f=open(OUTPUT_FILE,"w")
    while i<=d:
        compiler.Output=""
        compiler.CurrentChar="start"
        while length>len(compiler.Output) or (not compiler.withCustomLength):
            if (compiler.withCustomLength) and "end" in compiler.DATA[compiler.LANGUAGE]["weights"][compiler.CurrentChar].keys():
                if compiler.DATA[compiler.LANGUAGE]["weights"][compiler.CurrentChar]["end"] == 1.0:
                    break
                else: del compiler.DATA[compiler.LANGUAGE]["weights"][compiler.CurrentChar]["end"]
            char=''.join(random.choices(compiler.loadKeys(),weights=compiler.loadValues()))
            if char=="end":
                break
            compiler.CurrentChar=char
            compiler.Output+=compiler.CurrentChar
            
        if withoutput_file:f.write(compiler.Output+"\n")
        print(" |",compiler.Output)
        i+=1
    print(" |=========================>>> ")
    
if __name__=="__main__":
    main()
    

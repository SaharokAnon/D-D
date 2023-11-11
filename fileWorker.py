import os.path
from os import path
import json
from character import Charecter

class FileWorker():

    def __init__(self, char = None):
        if char is not None:
            self.char = char
    
    def write_to_file(self):
        charDict = {"title" : "CHARACTER", "data" : self.char.scores}
        dmpdChar = json.dumps(charDict, ensure_ascii=False)
        self.fp = open("chars/" + self.char.name + ".dnd", 'w+')
        self.fp.write(dmpdChar)
        fp.close()
    
    def read_from_file(self, charName):
        self.fp = open("chars/" + self.char.name + ".dnd", "r+")
        tmp = self.fp.read()
        tmp = json.loads(tmp)
        #print(self.fp.read())
        print(tmp['title'])
        self.fp.close()

lol = Charecter(name='Romass', race='Эльф', clas='воин')
fwLol = FileWorker(lol)
#fwLol.write_to_file()
fwLol.read_from_file("Romass")
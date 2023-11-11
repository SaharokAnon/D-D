import os.path
from os import path
import character.py

class FileWorker():

    def _init_(self, char):
        self.char = char
        if path.exists(char.name + ".dnd"):
            f = open(char.name + ".dnd", '+')
    
    def write_to_file():
        charDict = {"title" : "CHARACTER", "data" : self.char.scores}
        dmpdChar = json.dump(charDict, ensure_ascii=False)

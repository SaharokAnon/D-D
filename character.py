class Charecter():
    

    def __init__(self, name, race, clas):
        self.name = name
        self.race = race
        self.clas = clas
        self.mainscor = dict(сила =0,ловкость = 0,телосложение =0, инт =0,мудрость =0,харизма =0)  #сила, ловкость, телосложение, инт, мудрость, харизма
        self.selfthrow = [0,0,0,0,0,0] #сила, ловкость, телосложение, инт, мудрость, харизма
        self.mhp = 0
        self.cd = 0
        self.skil = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #акробатика(лов)   анализ(инт)   атлетика (сил)   восприятие(муд)  выживание(муд)  выступление(хар)   запугивание (хар)    история(инт)  ловкость рук(лов)    магия(инт)   медицина(муд)   обман(хар)   природа(инт)   проницательность(муд)   религия(инт)   скрытность(лов)   убеждение(хар)    уход за животными(муд) 
        self.masterbonus = 2
        self.scores = dict(
         воин = dict(startScore = [3,2,2,-1,0,1], bestScore = [0,2], startMaxHp = 10),
         паладин = dict(startScore = [1,0,2,-1,3,2], bestScore = [4,5], startMaxHp = 10),
         лучник = dict(startScore = [2,3,1,-1,2,0], bestScore = [0,1], startMaxHp = 10),
         плут = dict(startScore = [-1,3,0,2,1,2], bestScore = [1,3], startMaxHp = 8)
         )
#генерит основные характеристики
    def mainscorreset(self):
        self.mainscor = self.scores[self.clas]['startScore']
        return self.mainscor
#генерит спасброски
    def selfthrowgen(self):
        self.selfthrow = self.mainscor
        self.selfthrow[self.scores[self.clas]['bestScore'][0]] = self.selfthrow[0] + self.masterbonus
        self.selfthrow[self.scores[self.clas]['bestScore'][1]] = self.selfthrow[0] + self.masterbonus
        return self.selfthrow

    def mheltpoint(self):
        self.mhp = self.scores[self.clas]['startMaxHp']
        return self.mhp
    
    def skils(self):
        self.skil[0] = self.mainscor[0]
        return self.skil

lol = Charecter(name='Roma', race='Эльф', clas='воин')
print(lol.mainscorreset())
print(lol.selfthrowgen())
print(lol.mheltpoint())
print(lol.name + " " +lol.clas)
class Charecter():
    

    def __init__(self, name, race, clas):
        self.name = name
        self.race = race
        self.clas = clas
        self.mainscor = [0,0,0,0,0,0]  #сила, ловкость, телосложение, инт, мудрость, харизма
        self.selfthrow = [0,0,0,0,0,0] #сила, ловкость, телосложение, инт, мудрость, харизма
        self.mhp = 0
        self.cd = 10
        self.skil = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
        self.masterbonus = 2
        self.scores = dict(
         воин = dict(startScore = [3,2,2,-1,0,1], bestScore = [0,2], startMaxHp = 10),
         паладин = dict(startScore = [1,0,2,-1,3,2], bestScore = [4,5], startMaxHp = 10),
         лучник = dict(startScore = [2,3,1,-1,2,0], bestScore = [0,1], startMaxHp = 10),
         плут = dict(startScore = [-1,3,0,2,1,2], bestScore = [1,3], startMaxHp = 8),
         человек = dict(addscor = [1,1,1,1,1,1]),
         гном = dict(addscor = [0,0,0,2,0,0]),
         эльф = dict(addscor = [0,2,0,0,0,0]),
         полурослик = dict(addscor = [0,2,0,0,0,0])
         )
#генерит основные характеристики
    def mainscorreset(self):
        for i in range(5):
            self.mainscor[i] = self.scores[self.clas]['startScore'][i] + self.scores[self.race]['addscor'][i]
        return self.mainscor
#генерит спасброски
    def selfthrowgen(self):
        self.selfthrow = self.mainscor
        self.selfthrow[self.scores[self.clas]['bestScore'][0]] = self.selfthrow[self.scores[self.clas]['bestScore'][0]] + self.masterbonus
        self.selfthrow[self.scores[self.clas]['bestScore'][1]] = self.selfthrow[self.scores[self.clas]['bestScore'][1]] + self.masterbonus
        return self.selfthrow
#генерируем очки здоровья
    def mheltpoint(self):
        self.mhp = self.scores[self.clas]['startMaxHp']
        return self.mhp
#генерируем навыки
    def skils(self):
        self.skil[0] = self.mainscor[0] #сила: атлетика 
        for i in range(3):
            self.skil[i+1] = self.mainscor[1] #ловкость: акробатика, ловкость рук, скрытность
        for i in range(5):
            self.skil[i+4] = self.mainscor[3] #интеллект: анализ, история, магия, природа, религия
        for i in range(4):
            self.skil[i+9] = self.mainscor[4] #мудрость: восприятие, выживание, медицина, проницательность, уход за животными
        for i in range(4):
            self.skil[i+14] = self.mainscor[5] #харизма: выступление, запугивание, обман, убеждение
        return self.skil
#очки защиты
    def defscor(self):
        self.cd = self.cd + self.mainscor[1]
        return self.cd

lol = Charecter(name='Roma', race='эльф', clas='воин')
print(lol.mainscorreset())
print(lol.selfthrowgen())
print(lol.mheltpoint())
print(lol.skils())
print(lol.defscor())
print(lol.name + " " +lol.clas)
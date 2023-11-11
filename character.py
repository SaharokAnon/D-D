class Charecter():
    

    def __init__(self, name, race, clas):
        self.name = name
        self.race = race
        self.clas = clas
        self.mainscor = dict(0,0,0,0,0,0)  #сила, ловкость, телосложение, инт, мудрость, харизма
        self.selfthrow = [0,0,0,0,0,0] #сила, ловкость, телосложение, инт, мудрость, харизма
        self.mhp = 0
        self.cd = 0
        self.skil = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #акробатика(лов)   анализ(инт)   атлетика (сил)   восприятие(муд)  выживание(муд)  выступление(хар)   запугивание (хар)    история(инт)  ловкость рук(лов)    магия(инт)   медицина(муд)   обман(хар)   природа(инт)   проницательность(муд)   религия(инт)   скрытность(лов)   убеждение(хар)    уход за животными(муд) 
        self.masterbonus = 2
        self.startscor = dict(воин = [3,2,2,-1,0,1], паладин =[1,0,2,-1,3,2], лучник = [2,3,1,-1,2,0], плут = [-1,3,0,2,1,2])
        self.bestscor = dict(воин = [0,2], паладин = [4,5], лучник = [0,1], плут = [1,3])
        self.startmaxhp = dict(воин = 10, паладин = 10, лучник = 10, плут = 8)
#генерит основные характеристики
    def mainscorreset(self):
        self.mainscor = self.startscor[self.clas]
        return self.mainscor
#генерит спасброски
    def selfthrowgen(self):
        self.selfthrow = self.mainscor
        self.selfthrow[self.bestscor[self.clas][0]] = self.selfthrow[0] + self.masterbonus
        self.selfthrow[self.bestscor[self.clas][1]] = self.selfthrow[0] + self.masterbonus
        return self.selfthrow

    def mheltpoint(self):
        self.mhp = self.startmaxhp[self.bestscor]
        return self.mhp
    
    def skils(self):
        self.skil[0] = self.mainscor[0]
        return self.skil

lol = Charecter(name='Roma', race='Эльф', clas='воин')
print(lol.mainscorreset())
print(lol.selfthrowgen())
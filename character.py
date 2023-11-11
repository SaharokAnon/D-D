class Charecter():
    

    def __init__(self, name, race, clas):
        self.name = name
        self.race = race
        self.clas = clas
        self.mainscor = [0,0,0,0,0,0]  #сила, ловкость, телосложение, инт, мудрость, харизма
        self.selfthrow = [0,0,0,0,0,0] #сила, ловкость, телосложение, инт, мудрость, харизма
        self.hp = 0
        self.cd = 0
        self.masterbonus = 2
        self.startscor = dict(воин = [3,2,2,-1,0,1], паладин =[1,0,2,-1,3,2], лучник = [2,3,1,-1,2,0], плут = [-1,3,0,2,1,2])
        self.bestscor = dict(воин = [0,2], паладин = [4,5], лучник = [0,1], плут = [1,3])

    def mainscorregul(self):
        self.mainscor = self.startscor[self.clas]
        return self.mainscor

    def selfthrowgen(self):
        self.selfthrow = self.mainscor
        self.selfthrow[self.bestscor[self.clas][0]] = self.selfthrow[0] + self.masterbonus
        self.selfthrow[self.bestscor[self.clas][1]] = self.selfthrow[0] + self.masterbonus
        return self.selfthrow

lol = Charecter(name='Roma', race='Эльф', clas='воин')
print(lol.mainscorregul())

print(lol.selfthrowgen())
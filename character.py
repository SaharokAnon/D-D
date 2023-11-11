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
        self.numclas = ['воин', 'паладин', 'лучник', 'плут']
        self.bests = [[3,2,2,-1,0,1],[1,0,2,-1,3,2],[2,3,1,-1,2,0],[-1,3,0,2,1,2]]

    def rol(self):
        for i in range(6):
            if (self.clas) == self.numclas[i]:
                self.numclas = i
                return self.numclas
        
    def mainscorregul(self):
        self.mainscor = self.bests[self.numclas]
        return self.mainscor

    def selfthrowgen(self):
        for i in range(6):
            self.selfthrow[i] = self.mainscor[i]
        return self.selfthrow
    

lol = Charecter(name='Roma', race='Эльф', clas='воин')
print(lol.mainscorregul())

print(lol.selfthrowgen())
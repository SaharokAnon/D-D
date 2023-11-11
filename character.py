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


    
    def mainscorregul(self):
        for i in range(6):
            self.mainscor[i] =+ random.randint(1,2)
        
        return self.mainscor

    def selfthrowgen(self):
        i = random.randint(0,5)
        self.selfthrow[i] =self.mainscor[i] + random.randint(1,2) + self.masterbonus 
        i =random.randint(0,5)
        self.selfthrow[i] = self.mainscor[i] + random.randint(1,2) + self.masterbonus 
        return self.selfthrow
    

lol = Charecter(name='Roma', race='lol', clas='chert')
print(lol.mainscorregul())

print(lol.selfthrowgen())
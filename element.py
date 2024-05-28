elements = ('Hydrogen:H', 'Helium:He', 'Oganesson:Og')
class Element:
    p = 0
    n = 0
    e = 0

    def __init__(self, protons, neutrons, electrons):
        self.p = protons
        self.n = neutrons
        self.e = electrons
    
    def isStable(self):
        return False

    def getName(self):
        return elements[self.p].split(':')[0]

    def getSymbol(self):
        return elements[self.p].split(':')[1]

    def getCharge(self):
        return self.p - self.e
    
    def getOrbital(self, orbital):
        return self.getOrbital(1, 1)

    def getOrbital(self, energyLevel, orbitalType):
        return 2


    
class orbital:

    def __init__(self, energyLevel):
        self.e = 0
        self.energyLevel = energyLevel
        self.capacity = 0

    def isFull(self):
        return self.e == self.capacity

    def stability(self):
        if self.e * 2 == self.capacity:
            return 2
        elif self.isFull():
            return 3
        else: 
            return 0

    def getElectrons(self):
        return self.e

    def __str__(self):
        return ""
    
    def add(self, electrons):
        self.e += int(electrons)

        if self.e > self.capacity:
            leftover = self.e - self.capacity
            self.e = self.capacity
            return leftover

        return 0

    

    
class orbitalS(orbital):
    def __init__(self, energyLevel):
        super().__init__(energyLevel)
        self.capacity = 2
    
    def __str__(self):
        if self.e > 0:
            return str(self.energyLevel) + "S^" + str(self.e) + ", "
        return ""
class orbitalP(orbital):
    def __init__(self, energyLevel):
        super().__init__(energyLevel)
        self.capacity = 6
    
    def __str__(self):
        if self.e > 0:
            return str(self.energyLevel) + "P^" + str(self.e) + ", "
        return ""
class orbitalD(orbital):
    def __init__(self, energyLevel):
        super().__init__(energyLevel)
        self.capacity = 10
    
    def __str__(self):
        if self.e > 0:
            return str(self.energyLevel) + "D^" + str(self.e) + ", "
        return ""
class orbitalF(orbital):
    def __init__(self, energyLevel):
        super().__init__(energyLevel)
        self.capacity = 12
    
    def __str__(self):
        if self.e > 0:
            return str(self.energyLevel) + "F^" + str(self.e) + ", "
        return ""

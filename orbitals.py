class orbital:

    def __init__(self, energyLevel):
        self.e = 0
        self.energyLevel = energyLevel
        self.capacity = 2

    def isFull(self):
        return self.e == self.capacity

    def stability(self):
        if self.e * 2 == self.capacity:
            return 2
        elif self.isFull():
            return 3
        else: 
            return 0
    
    def add(self, electrons):
        self.e += electrons #convert to int

        if self.e > self.capacity:
            leftover = self.e - self.capacity
            self.e = self.capacity
            return leftover

        return 0

    

    
class orbitalS(orbital):
    def __init__(self, energyLevel):
        super().__init__(energyLevel)
        self.capacity = 2

class orbitalP(orbital):
    def __init__(self, energyLevel):
        super().__init__(energyLevel)
        self.capacity = 6

class orbitalD(orbital):
    def __init__(self, energyLevel):
        super().__init__(energyLevel)
        self.capacity = 10

class orbitalF(orbital):
    def __init__(self, energyLevel):
        super().__init__(energyLevel)
        self.capacity = 12
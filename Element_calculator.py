'''
Element calculator - This single-file version exists to make it easier to, for instance, paste into an online compiler.
Contains classes for an atom and an orbital, and a main method

@author Silas W and Molly M
@version 6-5-2024
'''

# Orbital class - each type of orbital inherits from the base orbital class. Base class is only used to represent empty orbitals
class orbital:

    # Initializes empty orbital with its energy level
    # (overridden in child classes)
    def __init__(self, energyLevel):
        self.e = 0
        self.energyLevel = energyLevel
        self.capacity = 0

    # Getters
    def isFull(self):
        return self.e == self.capacity

    def getElectrons(self):
        return self.e

    # Finds stability of orbital - Where do electrons want to be
    #ADD: Implement (see electrostablilze())
    #ADD: Make it better (I wrote this in 1 min)
    def stability(self):
        if self.e * 2 == self.capacity:
            return 2
        elif self.isFull():
            return 3
        else: 
            return 0

    # Uses energy level, type, and electrons to find its part of the orbital form of an atom
    # (Overridden in child classes)
    def __str__(self):
        return ""
    
    #Adds electrons and returns leftover
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
            return str(self.energyLevel) + "S^" + str(self.e) + " "
        return ""
    

class orbitalP(orbital):
    def __init__(self, energyLevel):
        super().__init__(energyLevel)
        self.capacity = 6
    
    def __str__(self):
        if self.e > 0:
            return str(self.energyLevel) + "P^" + str(self.e) + " "
        return ""
    

class orbitalD(orbital):
    def __init__(self, energyLevel):
        super().__init__(energyLevel)
        self.capacity = 10
    
    def __str__(self):
        if self.e > 0:
            return str(self.energyLevel) + "D^" + str(self.e) + " "
        return ""
    

class orbitalF(orbital):
    def __init__(self, energyLevel):
        super().__init__(energyLevel)
        self.capacity = 12
    
    def __str__(self):
        if self.e > 0:
            return str(self.energyLevel) + "F^" + str(self.e) + " "
        return ""





# Element class - can find its name, symbol, charge, mass, orbitals, stability, and can decay

elements = ('Nothing:N/A', 'Hydrogen:H', 'Helium:He', 
    'Lithium:Li', 'Beryllium:Be', 'Boron:B', 'Carbon:C', 'Nitrogen:N', 'Oxygen:O', 'Fluorine:F', 'Neon:Ne', 
    'Sodium:Na', 'Magnesium:Mg', 'Aluminum:Al', 'Silicon:Si', 'Phosphorus:P', 'Sulfur:S', 'Chlorine:Cl', 'Argon:Ar', 
    'Potassium:K', 'Calcium:Ca', 'Scandium:Sc', 'Titanium:Ti', 'Vanadium:V', 'Chromium:Cr', 'Manganese:Mn', 'Iron:Fe', 'Cobalt:Co', 'Nickel:Ni', 'Copper:Cu', 'Zinc:Zn', 'Gallium:Ga', 'Germanium:Ge', 'Arsenic:As', 'Selenium:Se', 'Bromine:Br', 'Krypton:Kr',
    'Rubidium:Rb', 'Strontium:Sr', 'Yttrium:Y', 'Zirconium:Zr', 'Niobium:Nb', 'Molybdenum:Mo', 'Technetium:Tc', 'Ruthenium:Ru', 'Rhodium:Rh', 'Palladium:Pd', 'Silver:Ag', 'Cadmium:Cd', 'Indium:In', 'Tin:Sn', 'Antimony:Sb', 'Tellurium:Te', 'Iodine:I', 'Xenon:Xe', 
    'Caesium:Cs', 'Barium:Ba', 'Lanthanum:La', 'Cerium:Ce', 'Praseodymium:Pr', 'Neodymium:Nd', 'Promethium:Pm', 'Samarium:Sm', 'Europium:Eu', 'Gadolinium:Gd', 'Terbium:Tb', 'Dysprosium:Dy', 'Holmium:Ho', 'Erbium:Er', 'Thulium:Tm', 'Ytterbium:Yb', 'Lutetium:Lu', 'Hafnium:Hf', 'Tantalum:Ta', 'Tungsten:W', 'Rhenium:Re', 'Osmium:Os', 'Iridium:Ir', 'Platinum:Pt', 'Gold:Au', 'Mercury:Hg', 'Thallium:Tl', 'Lead:Pb', 'Bismuth:Bi', 'Polonium:Po', 'Astatine:At', 'Radon:Rn', 
    'Francium:Fr', 'Radium:Ra', 'Actinium:Ac', 'Thorium:Th', 'Protactinium:Pa', 'Uranium:U', 'Neptunium:Np', 'Plutonium:Pu', 'Americium:Am', 'Curium:Cm', 'Berkelium:Bk', 'Californium:Cf', 'Einsteinium:Es', 'Fermium:Fm', 'Mendelevium:Md', 'Nobelium:No', 'Lawrencium:Lr', 'Rutherfordium:Rf', 'Dubnium:Db', 'Seaborgium:Sg', 'Bohrium:Bh', 'Hassium:Hs', 'Meitnerium:Mt', 'Darmstadtium:Ds', 'Roentgenium:Rg', 'Copernicium:Cn', 'Nihonium:Nh', 'Flerovium:Fl', 'Moscovium:Mc', 'Livermorium:Lv', 'Tennessine:Ts', 'Oganesson:Og')
class Element:

    # Constructs atom using proton, neutron, and electron count
    # Fills orbitals very simply - just from top down
    def __init__(self, protons, neutrons, electrons):
        self.p = int(protons)
        self.n = int(neutrons)
        self.e = [  orbitalS(1), orbital(0),  orbital(0),  orbital(0),
                    orbitalS(2), orbital(0),  orbital(0),  orbitalP(2), 
                    orbitalS(3), orbital(0),  orbital(0),  orbitalP(3),
                    orbitalS(4), orbital(0),  orbitalD(3), orbitalP(4),
                    orbitalS(5), orbital(0),  orbitalD(4), orbitalP(5),
                    orbitalS(6), orbitalF(4), orbitalD(5), orbitalP(6),
                    orbitalS(7), orbitalF(5), orbitalD(6), orbitalP(7)]

        for o in self.e:
            electrons = o.add(int(electrons))

        self.electrostable()

    #Returns the stability or estimated type of decay for the current atom
    #ADD: Better estimations
    #ADD: See decay
    def getStable(self):
        x = ((self.p * self.p) / 194) + ((97 * self.p) / 92) #magic numbers
        
        if abs(x - self.n) < 4 - 2 * (self.p%2) and self.p < 83:
            return 0 #stable
        if self.p > 99 or (self.n < 130 and self.p > 81) or (abs(x - self.n) < 6 and self.p > 83):
            return 3 #too big and an exception - alpha decay
        if x - self.n > self.p / 3.3: 
            return -2 #proton decay
        if self.n - x > self.n / 2.5:
            return 2 #neutron decay
        return 1 if x > self.n else -1 #beta decay
    
    # Name getters - uses an array to get the name and symbol of an atom using its proton count
    #ADD: Case for more than 118 protons
    def getName(self):
        return elements[self.p].split(':')[0]

    def getSymbol(self):
        return elements[self.p].split(':')[1] + "-" + str(self.p + self.n)

    # Calculates charge using proton and electron count
    #ADD: Is this a stable ion? Does it exist naturally?
    def getCharge(self):
        e = 0
        for o in self.e:
            e += o.getElectrons()
        return self.p - e

    # Orbital getters - access the electron arrays as numbers or text
    def getOrbital(self, orbital):
        return self.e[orbital].e
    
    def getOrbitals(self):
        total = ""
        for o in self.e:
            total += str(o)
        return total
    
    #ADD: Stabilize electron orbitals - more than just fill top-down (see every transition metal ever)
    #ADD: Eject electrons if the charge gets too low (and add something for the reverse case?)
    def electrostable(self):
        return 0

    # Decay simulator - Uses stability estimate to decay the nucleus in some way
    # Returns stability after decay for redundancy
    #ADD: Fission (difficult)
    #ADD: Kaboom (easier) (if the atom shouldnt exist ever)
    #ADD: How much energy is emitted? (Hint: E = mc^2)
    def decay(self): 
        
        if self.getStable() == -2 or (self.n == 0 and not self.p == 0):#failsafe
            self.p -= 1
            print("Ejected a proton: PROTON DECAY")
            
        elif self.getStable() == 2 or (self.p == 0 and not self.n == 0):#faisafe
            self.n -= 1
            print("Ejected a neutron: NEUTRON DECAY")
            
        elif self.getStable() == 3:
            self.p -= 2
            self.n -= 2
            print("Ejected a He nucleus: ALPHA DECAY")
            
        elif self.getStable() == -1:
            self.n -= 1
            self.p += 1
            print("Ejected an electron: BETA- DECAY")

        elif self.getStable() == 1:
            self.n += 1
            self.p -= 1
            print("Ejected a positron: BETA+ DECAY")

        self.electrostable()

        return self.getStable()





# Main method - I chose to contain it in a main function bc I'm a c++ guy
# Constructs an atom, and runs down its decay chain
def main():
    print("Hello? Would you like to make an element!")
    lmnt = Element(input("How many protons? "), input("How many neutrons? "), input("How many electrons? "))
    
    print("Name: " + lmnt.getName())
    print("Symbol: " + lmnt.getSymbol())
    print("Charge: " + str(lmnt.getCharge()))
    print("Stable? " + ("Probably" if lmnt.getStable() == 0 else "Unlikely"))
    print("Orbitals: " + lmnt.getOrbitals())
    
    while (not(lmnt.getStable() == 0) and input("Simulate decay? [enter] ") == ""):
        print()
        lmnt.decay()
        print("Protons: " + str(lmnt.p))
        print("Neutrons: " + str(lmnt.n))
        print("Name: " + lmnt.getName())
        print("Symbol: " + lmnt.getSymbol())
        print("Charge: " + str(lmnt.getCharge()))
        print("Stable? " + ("Probably" if lmnt.getStable() == 0 else "Unlikely"))


main()
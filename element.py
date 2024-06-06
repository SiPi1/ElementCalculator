'''
Element class - can find its name, symbol, charge, mass, orbitals, stability, and can decay

@author Silas W and Molly M
@version 6-5-2024
'''
import orb

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
        self.e = [  orb.orbitalS(1), orb.orbital(0),  orb.orbital(0),  orb.orbital(0),
                    orb.orbitalS(2), orb.orbital(0),  orb.orbital(0),  orb.orbitalP(2), 
                    orb.orbitalS(3), orb.orbital(0),  orb.orbital(0),  orb.orbitalP(3),
                    orb.orbitalS(4), orb.orbital(0),  orb.orbitalD(3), orb.orbitalP(4),
                    orb.orbitalS(5), orb.orbital(0),  orb.orbitalD(4), orb.orbitalP(5),
                    orb.orbitalS(6), orb.orbitalF(4), orb.orbitalD(5), orb.orbitalP(6),
                    orb.orbitalS(7), orb.orbitalF(5), orb.orbitalD(6), orb.orbitalP(7)]

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

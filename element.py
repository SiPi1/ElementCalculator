import orbitals.py

elements = ('Hydrogen:H', 'Helium:He', 
    'Lithium:Li', 'Beryllium:Be', 'Boron:B', 'Carbon:C', 'Nitrogen:N', 'Oxygen:O', 'Fluorine:F', 'Neon:Ne', 
    'Sodium:Na', 'Magnesium:Mg', 'Aluminum:Al', 'Silicon:Si', 'Phosphorus:P', 'Sulfur:S', 'Chlorine:Cl', 'Argon:Ar', 
    'Potassium:K', 'Calcium:Ca', 'Scandium:Sc', 'Titanium:Ti', 'Vanadium:V', 'Chromium:Cr', 'Manganese:Mn', 'Iron:Fe', 'Cobalt:Co', 'Nickel:Ni', 'Copper:Cu', 'Zinc:Zn', 'Gallium:Ga', 'Germanium:Ge', 'Arsenic:As', 'Selenium:Se', 'Bromine:Br', 'Krypton:Kr',
    'Rubidium:Rb', 'Strontium:Sr', 'Yttrium:Y', 'Zirconium:Zr', 'Niobium:Nb', 'Molybdenum:Mo', 'Technetium:Tc', 'Ruthenium:Ru', 'Rhodium:Rh', 'Palladium:Pd', 'Silver:Ag', 'Cadmium:Cd', 'Indium:In', 'Tin:Sn', 'Antimony:Sb', 'Tellurium:Te', 'Iodine:I', 'Xenon:Xe', 
    'Caesium:Cs', 'Barium:Ba', 'Lanthanum:La', 'Cerium:Ce', 'Praseodymium:Pr', 'Neodymium:Nd', 'Promethium:Pm', 'Samarium:Sm', 'Europium:Eu', 'Gadolinium:Gd', 'Terbium:Tb', 'Dysprosium:Dy', 'Holmium:Ho', 'Erbium:Er', 'Thulium:Tm', 'Ytterbium:Yb', 'Lutetium:Lu', 'Hafnium:Hf', 'Tantalum:Ta', 'Tungsten:W', 'Rhenium:Re', 'Osmium:Os', 'Iridium:Ir', 'Platinum:Pt', 'Gold:Au', 'Mercury:Hg', 'Thallium:Tl', 'Lead:Pb', 'Bismuth:Bi', 'Polonium:Po', 'Astatine:At', 'Radon:Rn', 
    'Francium:Fr', 'Radium:Ra', 'Actinium:Ac', 'Thorium:Th', 'Protactinium:Pa', 'Uranium:U', 'Neptunium:Np', 'Plutonium:Pu', 'Americium:Am', 'Curium:Cm', 'Berkelium:Bk', 'Californium:Cf', 'Einsteinium:Es', 'Fermium:Fm', 'Mendelevium:Md', 'Nobelium:No', 'Lawrencium:Lr', 'Rutherfordium:Rf', 'Dubnium:Db', 'Seaborgium:Sg', 'Bohrium:Bh', 'Hassium:Hs', 'Meitnerium:Mt', 'Darmstadtium:Ds', 'Roentgenium:Rg', 'Copernicium:Cn', 'Nihonium:Nh', 'Flerovium:Fl', 'Moscovium:Mc', 'Livermorium:Lv', 'Tennessine:Ts', 'Oganesson:Og')
class Element:

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

    
    def getStable(self):
#3/368, 77/92

        
        if abs((((3 * self.p * self.p) / 368) + ((77 * self.p) / 92)) - self.n) < 2: #magic numbers
            return 0 #stable
        elif ((3 * self.p * self.p) / 368) + ((77 * self.p) / 92) < self.n:
            return 1 if self.n - self.p < self.p else 2 #beta- or neutron decay
        else:
                return -1 if self.p - self.n < self.n else -2 #beta+ or proton decay
        if self.p < 102:
            if abs((1.5 * self.p) - self.n) > (self.p / 8) + 5:
                return 2 if 1.5 * self.p < self.n else -2 #proton or neutron decay
            if self.p > 83 and self.n < 134:
                return 3 #alpha decay
            if abs((1.5 * self.p) - self.n) < 2:
                return 0 if self.p < 83 else 3 #stable or alpha decay (if its too big)
            else:
                if (1.5 * self.p) < self.n:
                    return 1
                else:
                    return -1
        
        return 3 #alpha decay


    def getName(self):
        return elements[self.p - 1].split(':')[0]

    def getSymbol(self):
        return elements[self.p - 1].split(':')[1]

    def getCharge(self):
        e = 0
        for o in self.e:
            e += o.getElectrons()
        return self.p - e

    def getOrbital(self, orbital):
        return self.e[orbital].e
    
    def getOrbitals(self):
        total = ""
        for o in self.e:
            total += str(o)
        return total

    def decay(self): #Energy emitted?
        if self.getStable() == 3:
            self.p -= 2
            self.n -= 2
            print("Ejected a He nucleus: APHA DECAY")
            
        elif self.getStable() == 2:
            self.p -= 1
            print("Ejected a proton: PROTON DECAY")
            
        elif self.getStable() == 1:
            self.n -= 1
            self.p += 1
            print("Ejected an electron: BETA- DECAY")

        elif self.getStable() == -1:
            self.n += 1
            self.p -= 1
            print("Ejected a positron: BETA+ DECAY")
            
        elif self.getStable() == -2:
            self.n -= 1
            print("Ejected a neutron: NEUTRON DECAY")

        return self.getStable()

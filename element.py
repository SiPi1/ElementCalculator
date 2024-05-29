elements = ('Hydrogen:H', 'Helium:He', 
    'Lithium:Li', 'Beryllium:Be', 'Boron:B', 'Carbon:C', 'Nitrogen:N', 'Oxygen:O', 'Fluorine:F', 'Neon:Ne', 
    'Sodium:Na', 'Magnesium:Mg', 'Aluminum:Al', 'Silicon:Si', 'Phosphorus:P', 'Sulfur:S', 'Chlorine:Cl', 'Argon:Ar', 
    'Potassium:K', 'Calcium:Ca', 'Scandium:Sc', 'Titanium:Ti', 'Vanadium:V', 'Chromium:Cr', 'Manganese:Mn', 'Iron:Fe', 'Cobalt:Co', 'Nickel:Ni', 'Copper:Cu', 'Zinc:Zn', 'Gallium:Ga', 'Germanium:Ge', 'Arsenic:As', 'Selenium:Se', 'Bromine:Br', 'Krypton:Kr',
    'Rubidium:Rb', 'Strontium:Sr', 'Yttrium:Y', 'Zirconium:Zr', 'Niobium:Nb', 'Molybdenum:Mo', 'Technetium:Tc', 'Ruthenium:Ru', 'Rhodium:Rh', 'Palladium:Pd', 'Silver:Ag', 'Cadmium:Cd', 'Indium:In', 'Tin:Sn', 'Antimony:Sb', 'Tellurium:Te', 'Iodine:I', 'Xenon:Xe', 
    'Caesium:Cs', 'Barium:Ba', 'Lanthanum:La', 'Cerium:Ce', 'Praseodymium:Pr', 'Neodymium:Nd', 'Promethium:Pm', 'Samarium:Sm', 'Europium:Eu', 'Gadolinium:Gd', 'Terbium:Tb', 'Dysprosium:Dy', 'Holmium:Ho', 'Erbium:Er', 'Thulium:Tm', 'Ytterbium:Yb', 'Lutetium:Lu', 'Hafnium:Hf', 'Tantalum:Ta', 'Tungsten:W', 'Rhenium:Re', 'Osmium:Os', 'Iridium:Ir', 'Platinum:Pt', 'Gold:Au', 'Mercury:Hg', 'Thallium:Tl', 'Lead:Pb', 'Bismuth:Bi', 'Polonium:Po', 'Astatine:At', 'Radon:Rn', 
    'Francium:Fr', 'Radium:Ra', 'Actinium:Ac', 'Thorium:Th', 'Protactinium:Pa', 'Uranium:U', 'Neptunium:Np', 'Plutonium:Pu', 'Americium:Am', 'Curium:Cm', 'Berkelium:Bk', 'Californium:Cf', 'Einsteinium:Es', 'Fermium:Fm', 'Mendelevium:Md', 'Nobelium:No', 'Lawrencium:Lr', 'Rutherfordium:Rf', 'Dubnium:Db', 'Seaborgium:Sg', 'Bohrium:Bh', 'Hassium:Hs', 'Meitnerium:Mt', 'Darmstadtium:Ds', 'Roentgenium:Rg', 'Copernicium:Cn', 'Nihonium:Nh', 'Flerovium:Fl', 'Moscovium:Mc', 'Livermorium:Lv', 'Tennessine:Ts', 'Oganesson:Og')
class Element:

    def __init__(self, protons, neutrons, electrons):
        self.p = protons
        self.n = neutrons
        self.e = [  orbitalS(1), 
                    orbitalS(2),                           orbitalP(2), 
                    orbitalS(3),                           orbitalP(3),
                    orbitalS(4),              orbitalD(3), orbitalP(4),
                    orbitalS(5),              orbitalD(4), orbitalP(5),
                    orbitalS(6), orbitalF(4), orbitalD(5), orbitalP(6),
                    orbitalS(7), orbitalF(5), orbitalD(6), orbitalP(7)]

        for o in self.e:
            electrons = o.add(electrons)

    
    def isStable(self):
        if self.p < 20:
            return abs(self.p - self.n) < 2
        elif self.p < 83:
            return abs((1.5 * self.p) - self.n) < 2
        return False


    def getName(self):
        return elements[self.p].split(':')[0]

    def getSymbol(self):
        return elements[self.p].split(':')[1]

    def getCharge(self, orbital):
        return self.e[orbital].e
    
    def getOrbitals(self, orbital):
        orbitalSet = []
        orbitals = []
        for i in electrons:
            if(len(orbitalSet) < 4):
                a = 1

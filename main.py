import element.py

def main():
    print("Hello? Would you like to make an element!")
    element = Element(input("How many protons? "), input("How many neutrons? "), input("How many electrons? "))
    
    print("Name: " + element.getName())
    print("Symbol: " + element.getSymbol())
    print("Charge: " + str(element.getCharge()))
    print("Stable? " + ("Probably" if element.getStable() == 0 else "Unlikely"))
    print("Orbitals: " + element.getOrbitals())
    
    while (not(element.getStable() == 0) and input("Simulate decay? [Y/n] ") == "Y"):
        print()
        print("Protons: " + element.p)
        print("Neutrons: " + element.n)
        print("Name: " + element.getName())
        print("Symbol: " + element.getSymbol())
        print("Charge: " + str(element.getCharge()))
        print("Stable? " + ("Probably" if element.getStable() == 0 else "Unlikely"))
``

main()

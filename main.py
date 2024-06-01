import element.py

def main():
    print("Hello? Would you like to make an element!")
    element = Element(input("How many protons?"), input("How many neutrons?"), input("How many electrons?"))
    print("Name: " + element.getName())
    print("Symbol: " + element.getSymbol())
    print("Charge: " + str(element.getCharge()))
    print("Stable? Probably ")
    if not(element.isStable()):
        print("not")
    print("Orbitals: " + element.getOrbitals())


main()

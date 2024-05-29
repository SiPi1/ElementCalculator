def main():
    print("Hello? Would you like to make an element!")
    element = Element(input("How many protons?"), input("How many neutrons?"), input("How many electrons?"))
    print("Name: " + element.getName())
    print("Symbol: " + element.getSymbol())
    print("Charge: " + element.getCharge())
    print("Stable? " + element.isStable())


main()
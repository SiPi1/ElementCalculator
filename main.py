''' --RUN THIS FILE--
Main method - I chose to contain it in a main function bc I'm a c++ guy
Constructs an atom, and runs down its decay chain


@author Silas W
@version 6-5-2024
'''
import element

def main():
    print("Hello? Would you like to make an element!")
    lmnt = element.Element(input("How many protons? "), input("How many neutrons? "), input("How many electrons? "))
    
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

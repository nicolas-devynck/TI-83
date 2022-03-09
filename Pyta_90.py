import math
def function():
    print("----------")
    print("Verifier un angle droit")
    print("Donne la mesure que doit faire l'hypotenuse selon a et b")
    print("----------")
    print("A**2+B**2=C**2")
    print("----------")
    a=int(input("A ? "))
    b=int(input("B ? "))
    resultat = str(math.sqrt(a**2+b**2))
    return resultat
print("Hypotenuse = "+function())
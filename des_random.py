from random import *
# retourne un chiffre entre 1 et x*/
def d(x):
    x=randint(1,int(x)) 
    return x
print(d(input("x ? ")))

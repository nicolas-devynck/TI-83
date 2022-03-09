from random import *
def d(x):
    # tire un chifre aleatoire entre 1 et x
    x=randint(1,int(x))
    return x
print(d(input("x ? ")))
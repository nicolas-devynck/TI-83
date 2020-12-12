import math
def bin_dec():
    x = input("x ? ")
    resultat = int(0)
    k = int(1)
    for i in x:
        resultat = resultat + int(i)*2**int(len(x)-k)
        k = k+1
    return resultat
print(bin_dec())
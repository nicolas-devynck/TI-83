import math
def hex_dec():
    x = input("x ? ")
    resultat = int(0)
    k = int(1)
    for i in x:
        if i == "A":
            i = "10"
        elif i == "B":
            i = "11"
        elif i == "C":
            i = "12"
        elif i == "D":
            i = "13"
        elif i == "E":
            i = "14"
        elif i == "F":
            i = "15"
        resultat = resultat + int(i)*16**int(len(x)-k)
        k = k+1
    return resultat
print(hex_dec())
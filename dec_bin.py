import math
def dec_bin(x):
    resultat = ""
    tmp = str(int(math.fmod(int(x),2)))
    y = int(x)/2
    while (y>0):
        tmp = tmp + str(int(math.fmod(y,2)))
        y = int(y/2)
    for i in tmp:
        resultat=i+resultat
    return resultat
print(dec_bin(input("x ? ")))
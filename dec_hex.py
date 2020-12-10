import math
# voire dec_bin.py. meme algo =! basse 16
# + condtion pour l'hex (A = 10, b = 11, etc)
def dec_hex():
    x = int(input("x ? "))
    tmp = str(int(math.fmod(x,16)))
    y = int(x/16)
    if tmp == "10":
        tmp = "A"
    elif tmp == "11":
        tmp = "B"
    elif tmp == "12":
        tmp = "C"
    elif tmp == "13":
        tmp = "D"
    elif y == "14":
        tmp = "E"
    elif tmp == "15":
        tmp = "F"
    while (y>0):
        if str(int(math.fmod(y,16))) == "10":
            tmp = str(tmp) + "A"
        elif str(int(math.fmod(y,16))) == "11":
            tmp = str(tmp) + "B"
        elif str(int(math.fmod(y,16))) == "12":
            tmp = str(tmp) + "C"
        elif str(int(math.fmod(y,16))) == "13":
            tmp = str(tmp) + "D"
        elif str(int(math.fmod(y,16))) == "14":
            tmp = str(tmp) + "E"
        elif str(int(math.fmod(y,16))) == "15":
            tmp = str(tmp) + "F"
        else:
            tmp = str(tmp) + str(int(math.fmod(y,16)))
        y = int(y/16)
    resultat=""
    for i in tmp:
        resultat=i+resultat
    return resultat
print(dec_hex())
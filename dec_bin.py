import math
def dec_bin():
    # x = chifire a couvertire
    # tmp = suite des modulo ajouter a la suite les un des autre mais inversé
    # y = resulta de la division (sans virgule grace a int())
    # -----
    # innisialitaiotn des variable par un 1er calcule
    x = int(input("x ? "))
    tmp = int(math.fmod(x,2)) # x devient inutile (update posible) (%2)
    y = int(x/2) #(/2)
    while (y>0):
        tmp = str(tmp) + str(int(math.fmod(y,2))) #str() pour convertire un int en string et de pas faire 1+1 = 2 mais 1+1 = 11 (merci jcvd)
        y = int(y/2)
    # creation de la variable return
    # remetre dans l'ordre tmp dans resultat
    resultat=""
    # i in tmp =! tmp in i
    # on prend le dergnier caractaire pour le maitre ne 1er
    # l'avent dergnier pour le second etc
    for i in tmp:
        resultat=i+resultat
    return resultat
print(dec_bin())
# je sais il y a plus de #com que de ligne de code mais c'est pas ton probleme et je t'emerde c'est moi qui code
# si t'est pas contant ubisfot emboche
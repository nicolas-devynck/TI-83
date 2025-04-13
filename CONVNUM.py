from ti_system import *
from math import *
def hex_dec(x:str):
  resultat=int(0)
  k=int(1)
  for i in x:
    if i=="A" or i=="a":
      i="10"
    elif i=="B" or i=="b":
      i="11"
    elif i=="C" or i=="c":
      i="12"
    elif i=="D" or i=="d":
      i="13"
    elif i=="E" or i=="e":
      i="14"
    elif i=="F" or i=="f":
      i="15"
    resultat=resultat+int(i)*16**(len(x)-k)
    k=k+1
  return str(resultat)
def dec_hex(x:str):
  t = str(int(fmod(int(x),16)))
  y = int(int(x)/16)
  if t=="10":
    t="A"
  elif t=="11":
    t ="B"
  elif t=="12":
    t="C"
  elif t=="13":
    t="D"
  elif t=="14":
    t="E"
  elif t=="15":
    t="F"
  while (y>0):
    f=str(int(fmod(int(y),16)))
    if f=="10":
      t=t+"A"
    elif f=="11":
      t=t+"B"
    elif f=="12":
      t=t+"C"
    elif f=="13":
      t=t+"D"
    elif f=="14":
      t=t+"E"
    elif f=="15":
      t=t+"F"
    else:
      t=t+f
    y=int(int(y/16))
  resultat=""
  for i in t:
    resultat=i+resultat
  return resultat
def bin_dec(x:str):
  resultat=int(0)
  k=int(1)
  for i in x:
    resultat=resultat+int(i)*2**int(len(x)-k)
    k=k+1
  return str(resultat)
def dec_bin(x:str):
  resultat=""
  t=str(int(fmod(int(x),2)))
  y=int(int(x)/2)
  while (y>0):
    t=t+str(int(fmod(y,2)))
    y=int(y/2)
  for i in t:
    resultat=i+resultat
  return resultat
def choix(K):
  if K==143:#1
    disp_clr()
    print("BINAIRE -> DECIMAL")
    print("Entrez Q/Quitter ou R/Retour.")
    while 1:
      print("--------------------------------")
      QR=input("X : ")
      if QR=="Q" or QR=="q":
        disp_clr()
        return
      elif QR=="R" or QR=="r":
        main()
      else:
        print("Y : "+bin_dec(QR))
  elif K==144:#2
    disp_clr()
    print("DECIMAL -> BINAIRE")
    print("Entrez Q/Quitter ou R/Retour.")
    while 1:
      print("--------------------------------")
      QR=input("X : ")
      if QR=="Q" or QR=="q":
        disp_clr()
        return
      elif QR=="R" or QR=="r":
        main()
      else:
        print("Y : "+dec_bin(QR))
  elif K==145:#3
    disp_clr()
    print("HEXADECIMAL -> DECIMAL")
    print("Entrez Q/Quitter ou R/Retour.")
    while 1:
      print("--------------------------------")
      QR=input("X : ")
      if QR=="Q" or QR=="q":
        disp_clr()
        return
      elif QR=="R" or QR=="r":
        main()
      else:
        print("Y : "+hex_dec(QR))
  elif K==146:#4
    disp_clr()
    print("DECIMAL -> HEXADECIMAL")
    print("Entrez Q/Quitter ou R/Retour.")
    while 1:
      print("--------------------------------")
      QR=input("X : ")
      if QR=="Q" or QR=="q":
        disp_clr()
        return
      elif QR=="R" or QR=="r":
        main()
      else:
        print("Y : "+dec_hex(QR))
  elif K==147:#5
    disp_clr()
    print("HEXADECIMAL -> BINAIRE")
    print("Entrez Q/Quitter ou R/Retour.")
    while 1:
      print("--------------------------------")
      QR=input("X : ")
      if QR=="Q" or QR=="q":
        disp_clr()
        return
      elif QR=="R" or QR=="r":
        main()
      else:
        print("Y : "+dec_bin(hex_dec(QR)))
  elif K==148:#6
    disp_clr()
    print("BINAIRE -> HEXADECIMAL")
    print("Entrez Q/Quitter ou R/Retour.")
    while 1:
      print("--------------------------------")
      QR=input("X : ")
      if QR=="Q" or QR=="q":
        disp_clr()
        return
      elif QR=="R" or QR=="r":
        main()
      else:
        print("Y : "+dec_hex(bin_dec(QR)))
  elif K==151:#9
    disp_clr()
    return 
  else:
    choix(wait_key())
def main():
  disp_clr()
  print("CONVERTION NUMERIQUE")
  print("--------------------------------")
  print("1:Binaire -> Décimal")
  print("2:Décimal -> Binaire")
  print("3:Hexadécimal -> Décimal")
  print("4:Décimal -> Hexadécimal")
  print("5:Hexadécimal -> Binaire")
  print("6:Binaire -> Hexadécimal")
  print("9:Quitter")
  print("----Selectionez votre choix.----")
  choix(wait_key())
main()
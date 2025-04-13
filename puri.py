from math import *
from ti_system import *
def main():
  disp_clr()
  print("")
  print("{ P=Watt }------{ R=Ohm }-------")
  print("   1.R*I**2        7.P/I**2")
  print("   2.U*I           8.U**2/P")
  print("   3.U**2*R        9.U/I")
  print("{ U=Volt }------{ I=Ampère }----")
  print("   4.P/I           10.sqrt(P/R)")
  print("   5.sqrt(P*R)     11.P/U")
  print("   6.R*I           12.U/R")
  print("")
  choix(input("Selectionez... (Q/Quitter) : "))
def choix(x):
  if x=="1":
    disp_clr()
    print("---------{ P = R*I**2 }---------")
    while 1:
      R=input("R = ")
      if R=="q" or R=="Q" :
        main()
      I=input("I = ")
      if I=="q" or I=="Q" :
        main()
      print("P = "+str(float(R)*float(I)**2))
      print("--------------------------------")
  elif x=="2":
    disp_clr()
    print("-----------{ P = U*I }----------")
    while 1:
      U=input("U = ")
      if U=="q" or U=="Q" :
        main()
      I=input("I = ")
      if I=="q" or I=="Q" :
        main()
      print("P = "+str(float(U)*float(I)))
      print("--------------------------------")
  elif x=="3":
    disp_clr()
    print("---------{ P = U**2*R }---------")
    while 1:
      U=input("U = ")
      if U=="q" or U=="Q" :
        main()
      R=input("R = ")
      if R=="q" or R=="Q" :
        main()
      print("P = "+str(float(U)**2*float(R)))
      print("--------------------------------")
  elif x=="4":
    disp_clr()
    print("-----------{ U = P/I }----------")
    while 1:
      P=input("P = ")
      if P=="q" or P=="Q" :
        main()
      I=input("I = ")
      if I=="q" or I=="Q" :
        main()
      print("U = "+str(float(P)/float(I)))
      print("--------------------------------")
  elif x=="5":
    disp_clr()
    print("--------{ U = sqrt(P*R) }-------")
    while 1:
      P=input("P = ")
      if P=="q" or P=="Q" :
        main()
      R=input("R = ")
      if R=="q" or R=="Q" :
        main()
      print("U = "+str(sqrt(float(P)*float(R))))
      print("--------------------------------")
  elif x=="6":
    disp_clr()
    print("-----------{ U = R*I }----------")
    while 1:
      R=input("R = ")
      if R=="q" or R=="Q" :
        main()
      I=input("I = ")
      if I=="q" or I=="Q" :
        main()
      print("U = "+str(float(R)*float(I)))
      print("--------------------------------")
  elif x=="7":
    disp_clr()
    print("---------{ R = P/I**2 }---------")
    while 1:
      P=input("P = ")
      if P=="q" or P=="Q" :
        main()
      I=input("I = ")
      if I=="q" or I=="Q" :
        main()
      print("R = "+str(float(P)/float(I)**2))
      print("--------------------------------")
  elif x=="8":
    disp_clr()
    print("---------{ R = U**2/P }---------")
    while 1:
      U=input("U = ")
      if U=="q" or U=="Q" :
        main()
      P=input("P = ")
      if P=="q" or P=="Q" :
        main()
      print("R = "+str(float(U)**2/float(P)))
      print("--------------------------------")
  elif x=="9":
    disp_clr()
    print("-----------{ R = U/I }----------")
    while 1:
      U=input("U = ")
      if U=="q" or U=="Q" :
        main()
      I=input("I = ")
      if I=="q" or I=="Q" :
        main()
      print("R = "+str(float(U)/float(I)))
      print("--------------------------------")
  elif x=="10":
    disp_clr()
    print("--------{ I = sqrt(P/R) }-------")
    while 1:
      P=input("P = ")
      if P=="q" or P=="Q" :
        main()
      R=input("R = ")
      if R=="q" or R=="Q" :
        main()
      print("I = "+str(sqrt(float(P)/float(R))))
      print("--------------------------------")
  elif x=="11":
    disp_clr()
    print("-----------{ I = P/U }----------")
    while 1:
      P=input("P = ")
      if P=="q" or P=="Q" :
        main()
      U=input("U = ")
      if U=="q" or U=="Q" :
        main()
      print("I = "+str(float(P)/float(U)))
      print("--------------------------------")
  elif x=="12":
    disp_clr()
    print("-----------{ I = U/R }----------")
    while 1:
      U=input("U = ")
      if U=="q" or U=="Q" :
        main()
      R=input("R = ")
      if R=="q" or R=="Q" :
        main()
      print("I = "+str(float(U)/float(R)))
      print("--------------------------------")
  elif x=="q" or x=="Q":
    return 
  else:
    main()
main()
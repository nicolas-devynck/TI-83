from ti_system import *
from random import *
from time import *
disp_clr()
T=monotonic()
X=randint(1,100)
print("Trouvez X entre 1 et 100.")
print()
def D(I,C):
  C=C+int(1)
  if X==I:
    disp_clr()
    print("FELICITATION !!")
    print("---------------")
    print("Vous avez trouvé en "+str(C)+" coup(s)   et "+str(round(monotonic()-T))+" seconde.")
  elif X<I:
    print("Désoler X est plus petit.")
    print()
    D(int(input("Valeur de X ? ")),C)
  else:
    print("Désoler X est plus grand.")
    print()
    D(int(input("Valeur de X ? ")),C)
D(int(input("Valeur de X ? ")),int(0))
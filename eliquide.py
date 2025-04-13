from ti_system import *
import ti_plotlib as plt
def ELiquide(A,N):
  #total liquide calculer sur
  #15% et la qantiter de 'A'  
  T=A*100/15
  #total booster ml de 20mg/ml
  #regle de 3
  Bo=N*T/20
  #base pour completer
  #total - (arome + booster)
  Ba=T-(A+Bo)
  return [A,round(Bo),round(Ba),round(T),N]
disp_clr()
print("CALCULATRICE E-LIQUIDE")
print("--------------------------------")
A=int(input("Qantiter d'arome ? (ml) "))
N=int(input("Taux de nicotine ? (mg) "))
print("--------------------------------")
X=ELiquide(A,N)
#config
debut=120
fin=20
plt.color(0,0,0)
plt.cls()
plt.window(0,150,0,270)
plt.pen("thick","solid")
plt.line(debut-2,0,debut-2,270,"")
plt.line(debut+fin+1,0,debut+fin+1,270,"")
#arome
plt.color(100,0,155)
plt.line(95,175,100,175,"")

for i in range(fin):
  plt.line(debut+i,0,debut+i,X[0],"")
#booster
plt.color(230,0,0)
plt.line(95,150,100,150,"")

for i in range(fin):
  plt.line(debut+i,X[0],debut+i,X[1]+X[0],"")
#base
plt.color(0,200,100)
plt.line(95,125,100,125,"")

for i in range(fin):
  plt.line(debut+i,X[0]+X[1],debut+i,X[3],"")
#detail
print("")
print(" ---------------------")
print(" QANTITER")
print(" ---------------------")
print(" Arome : "+str(X[0])+" (ml)")
print(" Booster : "+str(X[1])+" (ml)")
print(" Base : "+str(X[2])+" (ml)")
print(" ---------------------")
print(" TOTAL : "+str(X[3])+" (ml)")
print(" ---------------------")
wait_key()
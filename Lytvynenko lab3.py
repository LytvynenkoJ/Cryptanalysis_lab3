import time
import gmpy2

#зчитуємо інформацію з файла
C=[]
n=[]
f = open("SE14.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]
f.close()

#обробляємо інформацію та заповнюємо масиви значень
for i in range(0, len(lines), 2):
    SrtC = lines[i].split(" = ")[1]
    SrtN = lines[i+1].split(" = ")[1]
    C.append(int(SrtC, base=16))
    n.append(int(SrtN, base=16))
    
#розширений алгоритм Евкліда необхідний для атак
def euclid(a, b):
    if a == 0 :
        return b,0,1
    r,u,v = euclid(b%a, a)
    x = v - (b//a) * u
    y = u
    return r,x,y

#атака з малою експонентою на основi китайської теореми про лишки
N=1
for i in range(len(n)):
    N*=n[i]
    
M=0
for i in range(3):
    Ni=N//n[i]
    v=euclid(Ni,n[i])[1]
    if v<0:
        v+=n[i]
    M+=C[i]*Ni*v
M = M%N
M=gmpy2.iroot(M, 3)

print(hex(int(M[0])))

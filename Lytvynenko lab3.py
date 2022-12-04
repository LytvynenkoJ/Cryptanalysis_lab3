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

#перевірки
for i in range(3):
    c=(M[0]**3)%n[i]
    c=int(c)
    print(c==C[i])

#зчитуємо дані для другої атаки
e = 65537
l = 20
f = open("MiM14.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]
f.close()
SrtC = lines[0].split(" = ")[1]
SrtN = lines[1].split(" = ")[1]
C=int(SrtC, base=16)
N=int(SrtN, base=16)

#починаємо відлік часу
start = time.perf_counter()

#готуємо допоміжну таблицю Х
X = []
for i in range(1,2**10+1):
    X.append((i**e)%N)
   
#Атака «зустрiч посерединi»
Sindex=0
Tindex=0
for i in range(1,2**10+1):
    S=euclid(X[i-1],N)[1]
    Cs=(C*S)%N
    if Cs in X:
        Sindex=i
        Tindex=X.index(Cs)+1
        break
M=Sindex*Tindex

#закінчуємо відлік часу
end = time.perf_counter()

print(hex(int(M)))

#перевірка
C1=(M**e)%N
print(C1==C)

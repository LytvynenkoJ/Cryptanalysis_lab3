# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:34:32 2022

@author: Yuliia
"""

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
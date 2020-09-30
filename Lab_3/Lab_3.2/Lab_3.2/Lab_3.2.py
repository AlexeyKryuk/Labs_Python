# -*- coding: utf-8 -*-
from math import *
from random import *

print("\n")

print("+---------------+-----------------------------------------------+")
print("|Крюков А.О.\t|\t\t\t\t\t\t|")
print("+---------------+  Лабораторная работа №3. Задание 2.\t\t|")
print("|ИВТм-201\t|\t\t\t\t\t\t|")
print("+---------------+-----------------------------------------------+")
print("|\t\t\t Попадание в мишень \t\t\t|")
print("+---------------------------------------------------------------|")

print("|\t X \t|\t Y \t|\t\t Res \t\t|")
print("+---------------------------------------------------------------+")

flag = 0
N = 15
r1 = 5
r2 = 8

for n in range(N):
 x = uniform(-5, 5)
 y = uniform(-8, 5)
 if (x < -r1) or (x > r2) or (y > r1) or (y < -r2): 
  flag = 0
 if (x >= -r1) and (x <= 0) and (y <= sqrt(r1 * r1 - x * x)) and (y >= 0) or (x >= 0) and (x <= r2) and (y <= -(sqrt(r1 * r1 - x * x))) and (y >= -(sqrt(r2 * r2 - x * x))):
  flag = 1
 else:
  flag = 0

 print("|{0: 7.2f}\t|{1: 7.2f}\t|".format(x, y), end=" ")
 if flag:
  print("\t\tYes\t\t|")
 else:
  print("\t\tNo\t\t|")

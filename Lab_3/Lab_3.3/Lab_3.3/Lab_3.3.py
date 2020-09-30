# -*- coding: utf-8 -*-
from math import *

print('Введите Xbeg, Xend, Dx и Eps')

xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))
eps = float(input('Eps='))

print("+---------------+-----------------------------------------------+")
print("|Крюков А.О.\t|\t\t\t\t\t\t|")
print("+---------------+  Лабораторная работа №3. Задание 3.\t\t|")
print("|ИВТм-201\t|\t\t\t\t\t\t|")
print("+---------------+-----------------------------------------------+")
print("|\t\t\t Вычисление функции эпсилон \t\t|")
print("+---------------------------------------------------------------|")

print("|\t X \t|\t Y \t|\t\t N \t\t|")
print("+---------------------------------------------------------------+")

xt = xb

while xt <= xe:
 an = xt
 n = 0
 y = an
 while True:
  k = -(xt**2) / (n + 1)
  an = an*k
  y = y + an
  n = n + 1
  if abs(an) < eps:
   break
 print("|{0: 7.2f}\t|{1: 7.3f}\t| \t{2: 4} \t\t\t|".format(xt,y,n))
 xt = xt + dx

print("+---------------------------------------------------------------+")

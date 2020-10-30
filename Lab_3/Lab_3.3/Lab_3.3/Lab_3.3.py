# -*- coding: utf-8 -*-
from math import *
from math import exp

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

print("|\t X \t|\t Y \t|\t N \t|\t f(x) \t|")
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
 print("|{0: 7.2f}\t|{1: 7.7f}\t| {2:} \t| {3: 4.7f}\t|".format(xt,y,n, exp(-(xt**2))))
 xt = xt + dx

print("+---------------------------------------------------------------+")

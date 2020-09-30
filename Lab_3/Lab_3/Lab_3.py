# -*- coding: utf-8 -*-
from math import *

print('Введите Xbeg, Xend и Dx')

xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))

xt = xb

print("\n")

print("+---------------+-----------------------------------------------+")
print("+Крюков А.О.\t+\t\t\t\t\t\t+")
print("+---------------+  Лабораторная работа №3.Организация циклов.\t+")
print("+ИВТм-201\t+\t\t\t\t\t\t+")
print("+---------------+-----------------------------------------------+")
print("+\t Значения функции от {:.3f} до {:.3f} с шагом {:.3f} \t+".format(xb, xe, dx))
print("+---------------------------------------------------------------+")

while xt <= xe:
 if xt >= -5 and xt < -3:
    y = xt + 3
 elif xt >=-3 and xt < 0:
    y = sqrt(9 - xt * xt)
 elif xt >= 0 and xt <= 6:
    y = 3 - 0.5 * xt
 elif xt > 6 and xt <= 9:
    y = xt - 6

 print("|\t{0: 7.2f}\t\t\t|\t{1: 7.2f}\t\t\t|".format(xt, y))
 xt += dx

print("+---------------------------------------------------------------+")
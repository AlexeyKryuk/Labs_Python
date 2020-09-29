# -*- coding: utf-8 -*-
from math import *

x = float(input('Введите значение x от -5 до 9: '))

if x >= -5 and x < -3:
	y = x + 3
elif x >= -3 and x < 0:
	y = sqrt(9 - x * x)
elif x >= 0 and x <= 6:
	y = 3 - 0.5 * x
elif x > 6 and x <= 9:
	y = x - 6
else:
	print('Введите корректное значение x: ')

print("y = {:.3f} x = {:.3f}".format(y, x))

x = float(input('Введите значение x: '))
y = float(input('Введите значение y: '))
r1 = float(input('Введите значение r1: '))
r2 = float(input('Введите значение r2: '))

if (x < -r1) or (x > r2) or (y > r1) or (y < -r2):
	flag = 0
if (x >= -r1) and (x <= 0) and (y <= sqrt(r1 * r1 - x * x)) and (y >= 0) or (x >= 0) and (x <= r2) and (y <= -(sqrt(r1 * r1 - x * x))) and (y >= -(sqrt(r2 * r2 - x * x))):
	flag = 1
else:
	flag = 0

print("Точка X = {:.3f}, точка Y = {:.3f}".format(x, y), end=" ")

if flag:
	print("попадает", end=" ")
else:
	print("не попадает", end=" ")

print("в область.")
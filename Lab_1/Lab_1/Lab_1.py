# -*- coding: utf-8 -*-
from math import *

alpha = float(input('Введите параметр alpha: '))
betta = float(input('Введите параметр betta: '))

z1 = (sin(alpha) + cos(2 * betta - alpha)) / (cos(alpha) - sin(2 * betta - alpha))
z2 = (1 + sin(2 * betta)) / (cos(2 * betta))

print("z1 = {:.6f}".format(z1))
print("z2 = {:.6f}".format(z2))


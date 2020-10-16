# -*- coding: utf-8 -*-
from math import *
from random import *

n = int(input("Элементов в массиве(N <= 30) N: "))
if n > 30: n = 30
elif n < 0: n = 0

A = float(input("Введите значение А: "))
B = float(input("Введите значение B: "))

print("\nНачальное состояние")
mas = []
for i in range(n):
 mas.append(uniform(-5, 5))
 print("{0: 7.3f}".format(mas[i]), end=" ")

countOfAB = 0

for i in range(n):
 if mas[i] >= A and mas[i] <= B:
  countOfAB += 1

print("\n\nКоличество элементов массива, лежащих в диапазоне от ", A, " до ", B, ": ", countOfAB)

maxValueIndex = 0
for i in range(n):
    if mas[i] > mas[maxValueIndex]:
        maxValueIndex = i

sumAfterMaxValue = 0
for i in range(maxValueIndex + 1, n):
    sumAfterMaxValue += mas[i]

print("\nМаксимальный элемент: {0:.3f}".format(mas[maxValueIndex]))
print("Сумма элементов, расположенных после максимального элемента: {0:.3f}".format(sumAfterMaxValue))

#Сортировка
for i in range(n-1):
    for j in range(n-i-1):
        if abs(mas[j]) < abs(mas[j+1]):
            mas[j], mas[j+1] = mas[j+1], mas[j]

print("\nОтсортированный массив")
print(', '.join('{:.3f}'.format(f) for f in mas))
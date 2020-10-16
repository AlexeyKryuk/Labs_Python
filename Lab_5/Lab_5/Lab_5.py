import numpy as np
from math import *

def MakeMatr(m, n, a, b):
 Matr = (b-a)*np.random.random(size=(n,m)) + a
 return Matr

def PrintMatr(Matr):
 """ Печать матрицы """
 (nRow, nCol) = Matr.shape
 for Row in range(nRow):
     for Col in range(nCol):
         print("{0: 7.3f}".format(Matr[Row][Col]), end=" ")
     print()
 print()

def CyclicShift(Matr, k):
    (nRow, nCol) = Matr.shape
    nNextRow = nRow
    nNextCol = nCol
    firstRow = 0
    firstCol = 0
    
    while True:

        for i in range(k):
            firstElement = Matr[firstRow][firstCol]
            for i in range(firstRow, nRow - 1):
                Matr[i][firstCol] = Matr[i + 1][firstCol]
            for i in range(firstCol, nCol - 1):
                Matr[nRow - 1][i] = Matr[nRow - 1][i + 1]
            for i in range(nRow - 1, firstRow, -1):
                Matr[i][nCol - 1] = Matr[i - 1][nCol - 1]
            for i in range(nCol - 1, firstCol + 1, -1):
                Matr[firstRow][i] = Matr[firstRow][i - 1]
            Matr[firstRow][firstCol + 1] = firstElement
        
        nNextRow -= 2
        nNextCol -= 2
        if nNextRow < 2 and nNextCol < 2:
            break

        nRow -= 1
        nCol -= 1
        firstRow += 1
        firstCol += 1



n=int(input("Введите кол-во строк матрицы: "))
m=int(input("Введите кол-во столбцов матрицы: "))
k=int(input("Введите кол-во элементов сдвига: "))

MyMatr=MakeMatr(m, n, -5, 5) # Изготовить матрицу
PrintMatr(MyMatr)

CyclicShift(MyMatr, k)
PrintMatr(MyMatr)




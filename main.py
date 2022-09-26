from logging import exception
import math
from random import randint
from typing import Type


class Matrix:

    def __init__(self, n, m):
        self.matrix = self.get_matrix(n, m)

    def get_matrix(self, n, m):
        # if math.isnan(int(n)) or math.isnan(int(m)):
        #     return 'e'
        try:
            if n<0 or m<0:
                return 'e'
            matrix = [[None for j in range(m)] for i in range(n)]
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    matrix[i][j] = randint(-10, 10)
            return matrix
        except TypeError:
            return 'e'
    def get_readable_matrix_string(self, matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))
        return '\n'.join(strings)

    # Магические методы

    # Определяет поведение при вызове функции str() в т.ч. и print()
    def __str__(self):
        return self.get_readable_matrix_string(self.matrix)

    # Возвращает кол-во элементов
    def __len__(self):
        return len(self.matrix)
    
    # Определяет поведение при доступе к элементу класса
    def __getitem__(self, item):
        return self.matrix[item]
    
    # Определяет поведение при умножении
    def __mul__(self, other):
        if isinstance(other, Matrix):
            return self.get_readable_matrix_string(self.multiply(other))
        return self.get_readable_matrix_string([[num*other for num in row] for row in self.matrix])

    def __add__(self, other):
        return self.getSummarize(other)
    
    def __sub__ (self, other):
        return self.getSubtraction(other)
    
    # Магические методы

    ## Функция трнаспонирования с помощью zip (internal)
    def transpose(self, matrix):
        return [list(i) for i in zip(*matrix)]

    ## Возвращаем транспонированную в нужном виде
    def getTranspose(self):
        return self.get_readable_matrix_string(self.transpose(self.matrix))

    ## Преобразование в транспонированную 
    def doTranspose(self):
        self.matrix = self.transpose(self.matrix)

    def multiply(self, matrix):
        
        # if len(self.matrix[0]) != len(matrix):
        #     correct = True
        try:
            result = [[0 for j in range(len(matrix[i]))]
                    for i in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(matrix[0])):
                    for k in range(len(matrix)):
                        result[i][j] += self.matrix[i][k] * matrix[k][j]
            return result
        except IndexError:
            return 'e'

    def getMultiply(self, matrix):
        return self.get_readable_matrix_string(self.multiply(matrix))

    def summarize(self, matrix):
        try: 
            if len(self.matrix) != len(matrix) or len(self.matrix) != len(matrix):
                return 'e'
            result = [[0 for j in range(len(matrix[0]))]
                    for i in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    result[i][j] = self.matrix[i][j] + matrix[i][j]
            return result
        except TypeError:
            return 'e'

    def getSummarize(self, matrix):
        return self.get_readable_matrix_string(self.summarize(matrix))

    def subtract(self, matrix):
        try:
            if len(self.matrix) != len(matrix) or len(self.matrix) != len(matrix):
                return 'e'
            result = [[0 for j in range(len(matrix[0]))]
                    for i in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    result[i][j] = self.matrix[i][j] - matrix[i][j]
            return result
        except TypeError:
            return 'e'
        

    def getSubtraction(self, matrix):
        return self.get_readable_matrix_string(self.subtract(matrix))

m1 = Matrix(2, 3)
m2 = Matrix(3, 5)
print(m1, 'Матрица 1 \n')
print(m2, 'Матрица 2 \n')
print(m1*m2, '- результат умножения матриц')
print('-------------Сложение матриц-------------')
m1 = Matrix(2, 2)
m2 = Matrix(2, 2)
print(m1, 'Матрица 1 \n')
print(m2, 'Матрица 2 \n')
print(m1+m2)
print('-------------Вычитание матриц-------------')
print(m1-m2)
print('-------------Ошибка перемножения-------------')
m1 = Matrix(2, 3)
m2 = Matrix(4, 5)
print(m1, 'Матрица 1 \n')
print(m2, 'Матрица 2 \n')
print(m1*m2)
print('----------Транспонирование матрицы----------')
print(m1.getTranspose())
print('-------------Умножение на число-------------')
print(m1*3)
print('-------------Размер только число-------------')
m3 = Matrix(-1, 3)
print(m3)
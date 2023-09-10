import random

class Matrix:
    def __init__(self, num_rows, num_cols, max_value):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.data = [[random.randint(1, max_value) for _ in range(num_cols)] for _ in range(num_rows)]

    def display(self):
        for row in self.data:
            print(row)

# Ввод значений m, n и L от пользователя
m = int(input("Введите значение m (количество строк): "))
n = int(input("Введите значение n (количество столбцов): "))
L = int(input("Введите значение L (максимальное значение в столбцах): "))

# Создание матрицы с случайными значениями, где каждая колонка - число от 1 до L
matrix = Matrix(m, n, L)

print("Случайно заполненная матрица:")
matrix.display()

# Задача 3.1 Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения,
#       * заменять существующие значения,
#       * выводить число строк и колонок.



import random

class Matrix:

        def __init__(self, row, column):
            self.row = row
            self.column = column
            self.data = [[None for _ in range(column)] for _ in range(row)]

        def fill_matrix(self, row, column, row_max_value):
            self.row = row
            self.column = column
            self.data = [[random.randint(1, row_max_value) for _ in range(column)] for _ in range(row)]


        def get_value(self, row, column):
            return self.data[row-1][column-1]


        def new_value(self, row, column, value):
            self.data[row - 1][column - 1] = value

        def add_row(self):
            new_row = [0] * self.column
            self.data.append(new_row)
            self.row += 1

        def add_column(self):
            for row in self.data:
                row.append(0)
            self.column += 1


        def print_size(self):

            print('\nЧисло строк:', self.row)
            print('Число столбцов:', self.column)

        def display(self):
            for row in self.data:
             print(row)



print ("1. Cоздаем матрицу ")
m = Matrix(4, 8)
m.display()

n = int(input("\n2. Введите N - максимальное значение для заполнения матрицы: "))
# Заполняем матрицу случайными значениями, где каждая колонка - число от 1 до N
m.fill_matrix(4,8, n)
#
print("\n3. Случайно заполненная матрица:")
m.display()

# Подсчет числа строк и столбцов
m.print_size()

print(f"\n4. Получаем значение в ячейке (4, 6): {m.get_value(4, 6)}\n")

print ("5. Меняем это значение в матрице на 999: \n")
m.new_value(4, 6, 999)

print("6. Новая матрица:")
m.display()

# Добавление строки и столбца
m.add_row()
m.add_column()

print("\n6. Добавляем строку и столбец к матрице:")
m.display()

m.print_size()


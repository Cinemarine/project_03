# Задача 2.1.

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

#Решение

def maximum(n):
   maximum_list = n[0]
   for i in n:
       if i > maximum_list:
          maximum_list = i
   return (maximum_list)

def minimum(n):
   minimum_list = n[0]
   for i in n:
       if i < minimum_list:
          minimum_list = i
   return (minimum_list)

num_list = input('Введите список целых чисел в одну строку через пробел: ')
try:
  numbers_list = list(map(int, num_list.split()))
  print (
    f"{numbers_list} -> max = {maximum(numbers_list)}, "
    f"min = {minimum (numbers_list)}"
         )
except ValueError:
  print("Некорректный ввод!")
  num_list = input('Введите список целых чисел в одну строку через пробел: ')
  try:
      numbers_list = list(map(int, num_list.split()))
      print(
          f"{numbers_list} -> max = {maximum(numbers_list)}, "
          f"min = {minimum(numbers_list)}"
      )
  except ValueError:
      print("Некорректный ввод!")
  finally:
      print("Конец")




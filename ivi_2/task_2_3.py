# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!


#Решение

def switch_number (number):
 numb1 = {0:'Ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
 match number:
   case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
      return print (f"switch_it_up({number}) -> {numb1.get(number)}")
   case _:
      return print(f"switch_it_up({number}) -> None")


n = input('Введите цифру от 0 до 9: ')
try:
    n2 = int(n)
    switch_number(n2)

except ValueError:
 print("Некорректный ввод! Введите цифру от 0 до 9:")
 n = input()
 try:
     n2 = int(n)
     switch_number(n2)

 except ValueError:
     print("Некорректный ввод!")
 finally:
     print("Конец")






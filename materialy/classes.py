#Классы в Pyton
#Императивный стиль работы - набор инструкций для выполнения
# Объектно-ориентированное программирование -
# есть объекты (списки, строки, модуля, функции и тп)
# ООП - создание объектов и описание правил взаимодействия между ними
# атрибуты - характеристики объектов

# 1. Класс - Класс - инструкция по созданию объекта
# Этап создания класса - каждое новое слово с большой буквы (CamelCase)

class Kletka:
      content = 1
      cont_type = type(content)

      def add_s (self,obj):
          self.content = obj
          self.cont_type = type (obj)


# Создание экземпляра класса
A1 = Kletka()
A1.add_s(199)
print (A1.content, A1.cont_type)

class Row:
    def __init__(self, *args):
        self.args = args

    def __eq__(self, other):
        return isinstance(other, type (self)) and self.args == other.args

    def __hash__(self):
        return hash(self.args)

    def __add__(self, other):
        return self.args + other.args if isinstance(other, Row) else self.args + other

r1 = Row(8,2,3)
r2 = Row(1,2,3)

print ({r1:'ver', r2:'gr'})
# print( r1 + r2,'\n')
# print(r2 + (1,2), '\n')
#Что такое класс объекта - прмер на машинах
class Car:
    #Атрибут - переменные внутри класса
     koleso = 4
     dver = 4
     dvigatel = False
     color = "Pink"

# методы - что может объект (функции внутри класса)
#cвязанный метод класса - self по умолчанию
     def signal(self):
        print('bi-bi!')

     def start_1 (self, key):
        if key == "ключ":
           self.dvigatel = True
           return self.dvigatel

#Что такое экземпляр класса?
# Объект, созданный по классу с индивидуальной характеристикой
# Для использования класс нужно объявить
#

lexus1 = Car()
lexus2 = Car()
lexus3 = Car()
lexus4 = Car()

#Изменение атрибута объекта

lexus1.color = "green"
print (lexus1.color, lexus2.color)

#вызов метода экземпляра класса
lexus1.signal()
print(lexus1.start_1('ключ'))
print(lexus1.dvigatel)


#Метод __del__

class Truck:

       def __init__(self, *arg):
           print('Загружено в трак:')
           [print(f'   *{(i)}') for i in arg]


       def __del__(self):
            print('Конец погрузки')

Belaz = Truck ('Песок', 'Ящики', 'Щебень')

# Матрица в Pandas
import pandas
class Matrix:
       def __init__(self):
           self.df = pandas.DataFrame()

m1 = Matrix()
print (m1.df)
# модуль app.py - стартовый запуск скрипта

## Терминалогия
# Модуль - файл, в котором мы работаем. Модуль рассматривается как самостоятельный объект в Python
# Пакет - папка с модулями, которая содежит файл __init__
# Библиотека - набор пакетов и модулей, например Python Standart Library

# Фреймворк - потом!


# Импорт имен
# 1 просто импорт модуля
# практические примеры: import os, import sys

#Cтруктура модуля
# 1. импорты (import os)
# 2. Константы (PATH="C:\users\")  в верхнем регистре писать
# 3. функции (def, func (par):)
# 4. Тело циклвм- условия
# Переменные не держать в модуле
# Переменные-свейства фиксируются в класссах



import functions

# print(functions.sum_all(100, 20, 300))

# 2 импорт с синонином
# практические примеры: import pandas as pd, import numpy as np
import functions as f

# print(f.sum_all(100, 20, 300))

# 3 импорт конкретного имени (остнорожно, можно перекрыть имя)
# практичкий пример: from flask import Flask
from functions import sum_all

# print(sum_all(100, 20, 300))


# импорт из пакетов
# # 1 просто импорт из пакета
# import my_package.module_2

# my_package.module_2.foo_2()

# 2 импорт с синонимом
# практический пример: import matplotlib.pyplot as plt
import my_package.modu
import functions
print (functions.sum_all(100, 20,30))

# импорт модуля с синонимом
import functions as f
print (f.sum_all(100, 20,30))


# импорт конкретного имени!!! - осторожно, можно перекрыть имя

from functions import sum_all
print (sum_all(100, 20,30))






m2.foo_2()

# 3 импорт напрямую из пакета
import my_package.subpackage as sp

sp.foo_3()




# # что такое __name__?
# print(__name__)  # __main__
# print(f.__name__)  # functions
# # значит, если модуль называется __main__, то он является исполняемым


# запуск скрипта по имени модуля
if __name__ == '__main__':
    print('Запуск скрипта')
    print(f.get_topmgrs({'Sam':100000, 'Paul':50000}))
    print(sum_all(100, 20, 300))






# Структура модуля
# 1 импорты (import os)
# 2 константы (PATH='C:\Users\') - лучше без них
# 3 функции (def func(par):)
# 4 классы (class Person:)
# 5 тело цикла-условия

# переменые в модуле лучше не объявлять.
# переменные-свойства фиксируются в классах

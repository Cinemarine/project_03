# Модуль 2

from .module_1 import foo_1
#точка значит - искать файл module_1 в текущей папке

def foo_2():
    print('Вызвана foo_2 из my_package.module_2')

foo_1()
# Магические методы Пайтон
# класс Bucket
# __name__

# Разместить строки, имитирующие файлы в экземпляре класса Bucket
# index.html
# readme.md
# page_404.html

class Bucket:
    # Контейнер для хранения объектов облачного хранения
    # Логическая сущность, помогающая организовать хранение объектов

    def __init__(self, *, tutorial=None):
        self.content = []
        if tutorial != None:
            self.content.append('readme.md')

    def __str__(self):
        return 'Cодержимое: ' + ' ,'.join(self.content)

    # Проверка на истинность
    def __bool__(self):
       return self.content != []

    def add(self, obj):
        self.content.append(obj)


# print('Добавлен', obj)
#     self.content = obj

website = Bucket(tutorial=True)
website.add('index.html')
print(website.content)
print(website)

empty_bucket = Bucket()
print(bool(empty_bucket))
print(bool(website))
# #

# Поместить объект в бакет

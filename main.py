#txt = "For only {price:.1f} dollars!"
#print(txt.format(price = 49))
#rainbow = ['red', 'green', 'blue']

#rainbow.append('sky')

#rainbow[0] = 11
#print (rainbow)

#gradient = [ [4,5] , [7,9] ]
#print (gradient [1][1])
#print (list(range(0, 5)))
#x=["y",45,89,"t",45]
#print (x.count(45))
x= "Olla la la la"
print (list (x))
print (x.count("l"))
print (len(x))
z=['red, green, blue']
print(', '.join(z))

shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']
# а. Вставьте рыбу между горошком и рисом
shop_list.insert(2, "рыба")
print(shop_list)
#Добавьте фрукты из списка fruits в конец списка shop_list
fruits = ['Яблоко', 'Апельсин', 'Клубника']
shop_list=shop_list+fruits
print(shop_list)
# c. Удалите из списка shop_list картофель
shop_list.remove('Картофель')
print(shop_list)
del shop_list[0]
print(shop_list)
# d. Какими по счету стоят хлеб и апельсин? Выведите номера на консоль в формате

print("Номер продукта 'хлеб' в списке", shop_list.index('Хлеб'))
print("Номер продукта 'апельсин'в списке", shop_list.index('Апельсин'))
print ("Задача 2")
city=['Москва','Питер','Тула','Ростов','Воронеж']
peoples=[
["Москва", 8],
["Питер", 4],
["Тула", 0.4],
["Воронеж", 1]
 ]
print (city)
print (peoples)
print('Население города', city[2],'–',peoples[2][1],'млн человек')
total=peoples [0][1]+peoples [1][1]+peoples [2][1]+peoples [3][1]
print ("Общее население –", (total), 'млн человек')

dog = 'жужа'
pet = dog
pet= pet.replace('ж', 'м')
print(dog,'\n',pet)


num = (20, 30, 40)
num + (50, 60)
print(num)

x, y, z = 1, 2, 3
(x, y, z) = (1, 2, 3)
print (x, y, z)

capitals = { }
capitals['Россия'] = 'Москва'
capitals['Франция'] = 'Париж'
print (capitals['Россия'])
vocabulary = { 'а' : ('ананас', 'апельсин', 'арбуз'),
'б' : ('баклажан','батат', 'брюква') }
book = vocabulary
book['в'] = ('виноград')
print(vocabulary,'\n',book)
print (capitals.get('Италия', 'Отсутствует'))
capitals.setdefault ('Италия')
print (capitals)
x=-1
print('Здравствуйте!')
if x < 0:
  print('Меньше нуля')

elif x == 1:
  print('Равно единице')
else:
  print('Больше нуля, но не равно единице')

print('До свидания!')

x, y = 4, 20
if x > y:
    print('x > y')
if x > y and x > 0:
    print('успех')
if 5 < y < 10:
    print('успех')

if '6' != 5:
    print('успех')

i=1
while i <= 10:
    print('i =', i)
    i += 1

print('Конец!')

#fib1, fib2 = 1, 1
#n = input('Номер элемента ряда Фибоначчи: ')
#n = int(n)
#i=0
#while i < n - 2:
    #print(fib2)
    #next_fib2 = fib1 + fib2
    #next_fib1 = fib2
    #fib1, fib2 = next_fib1, next_fib2
    #i += 1
#print('Значение этого элемента: ', fib2)


print('Здравствуйте!')
room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17,]
print (len(room_prices))
i=-1
while i < len(room_prices)-1:
    i += 1
    price = room_prices[i]
    print('Проверяем ', price)
    if price == min(room_prices):
        print('Найдена минимальная цена')
        break
print('Конец!')

print('Hello!')
hotel_names = list()
hotel_names.append('aloHotel')
hotel_names.append('Appart lounge')
hotel_names.append('Sleepower')
hotel_names.append('Penthouseus')
hotel_names.append('Hotel star')
print(hotel_names)
i = -1
while i < len(hotel_names):
    i += 1
    if i == 2:
        continue
    name = hotel_names[i]
    print('Проверяем', name)
    if name == 'Hotel star':
        print('Отель найден!')
        break
print('До свидания')


while True:
    user_input = input('Введите “Перерыв” >> ')
    result = str(user_input)
    if result == "yy":
        print('Урааа!')
        break
    else:
        print('А когда перерыв?( Попробуйте еще раз...')






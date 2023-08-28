

# Задача 2-1 решение while

# spis =[2, -1, 8,-5, 7]
# i=0
# total = 0
# while i < len(spis):
#    if spis[i] >= 0:
#          total+= spis[i]
#    i+=1
#
# print(total)
#
# # Задача 2-2 решение с for
#
# spis =[2, -1, 8,-5, 7]
#
# total = 0
# for a in spis:
#    if a >= 0:
#         total += a
#
# print(total)
#
#
#
# # Задача 2-3 решение с for индексы
#
# total=0
# for id in range(len(spis)):
#     if spis[id] >= 0:
#         total += spis[id]
#
# print(total)


# Задача 2-4 решение с for индексы функция
# total=0
# for id, elem in enumerate (spis):
#     if elem >= 0:
#       total += elem
#
# print(total)

# #Задача _1_1 Фибоначчи c while
# fib1, fib2 = 1, 1
# n = input('Номер элемента ряда Фибоначчи: ')
# n = int(n)
# i=0
# while i < n - 2:
#     print(fib2)
#     next_fib2 = fib1 + fib2
#     next_fib1 = fib2
#     fib1, fib2 = next_fib1, next_fib2
#     i += 1
# print('Значение этого элемента: ', fib2)

#Задача _1_2 Фибоначчи c for
# fib1, fib2 = 1, 1
# n = input('Номер элемента ряда Фибоначчи: ')
# n = int(n)
# for i in range (2,n):
#     fib1,fib2=fib2,fib1+fib2

# print('Значение этого элемента: ', fib2)
#
# #Задача _1_2 Фибоначчи c for
# fib1, fib2 = 1, 1
# n = input('Номер элемента ряда Фибоначчи: ')
# n = int(n)
# for i in range (2,n):
#     fib1,fib2=fib2,fib1+fib2
#
# print('Значение этого элемента: ', fib2)

# hotel_names = [ 'aloHotel', 'Appart lounge', 'Sleepower', 'Penthouseus', ]
# for name in hotel_names:
#     print(name)
#     del hotel_names[0]
# print(hotel_names)


room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]
for price in room_prices:
    if price == min (room_prices):
        continue
    if price == max (room_prices):
        print('Минимальная цена:', price)
        break
    print('Текущая цена:', price)
else:
        print('Такой цены нет!')
print('До свидания!')
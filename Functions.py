# Модуль для функций

Функция с нескоькими переменными
# Функция для добавления суперпользователя def add_root():

def add_root():
 name = 'root'
 uid = 0
 return name, uid

user_name, user_uid = add_root()

print(f'Имя пользователя {user_name}\nUID пользователя {user_uid}')


#Функция - блок кода, который можно вызывать с разными параметрами



empl1 = {'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121}
empl1.setdefault ('Pink')
empl1['Pink'] = (170000)

empl2 = {
    'Mar' : 90000,
    'Ken' : 130817,
    'Pip' : 80908,
    'Terry' : 180123,
    'Ven' : 193121}

def g_top(em):
   return [n for n, s in em.items() if s >= 100000]


g_top(empl1)
g_top(empl2)

print ([empl1[i]*2 for i in g_top(empl1)])

def make_coffee(size, sugar_dose=3):
  if sugar_dose > 5:
   return print('Слишком много сахара! :(')

  else:
   return print(f'Ваш кофе объемом {size} мл с {sugar_dose} кусочками сахара')

make_coffee(100, 2)
make_coffee(100, 8)

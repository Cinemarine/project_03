# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

# Решение
# 1. Заполняем таблицы

import sqlite3
connection = sqlite3.connect("Students_list_new.db")
cursor = connection.cursor()

# sql_query = """ CREATE TABLE IF NOT EXISTS Students
# ( Student_Id Integer NOT NULL PRIMARY KEY, Student_Name Text,
# School_Id Integer NOT NULL);"""
#
# sql_query2 = """ CREATE TABLE IF NOT EXISTS School_names
# ( School_Id INTEGER NOT NULL PRIMARY KEY, School_Name TEXT NOT NULL);"""

# sql_query3 = """INSERT OR IGNORE INTO Students (Student_Id, Student_Name, School_Id)
# VALUES
# (201, 'Иван', 11),
# (202, 'Петр', 12),
# (203, 'Анастасия', 13),
# (204, 'Игорь', 14),
# (205, 'Марина', 12),
# (206, 'Дмитрий', 11);"""

# sql_query4 = """INSERT OR IGNORE INTO School_names (School_Id, School_Name)
# VALUES
# (11, 'Гимназия им. Пирогова'),
# (12, 'Колледж Уникум'),
# (13, 'Гимназия Сколково'),
# (14, 'Школа Интеллект');"""

# cursor.execute(sql_query4)
# connection.commit()

# 2. По ID студента получаем информацию о школе и студенте.

def get_connect():
    connection = sqlite3.connect("Students_list_new.db")
    return connection

def close_connect(connection):
    if connection:
       connection.close()

def Student_ID_data(stud_ID):
    try:
        con = get_connect()
        cursor = con.cursor()
        sqlquery_n = """SELECT * FROM Students JOIN 
        School_names ON Students.School_Id = School_names.School_Id
        WHERE Students.Student_Id = ?"""
        cursor.execute(sqlquery_n, (stud_ID,))
        stud_nn = cursor.fetchall()
        for row in stud_nn:
            print("ID Cтудента: ", row[0])
            print("Имя Cтудента: ", row[1])
            print("ID школы:", row[2])
            print('Название школы:', row[4], '\n')
        close_connect(con)
    except (Exception, sqlite3.Error) as error:
        print("Ошибка - ", error)

St_data = int(input ('Введите ID cтудента (201-206): '))
Student_ID_data (St_data)
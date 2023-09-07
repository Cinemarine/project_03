# задача №1
# import sqlite3
# connection = sqlite3.connect("teachers1.db")
# cursor = connection.cursor()

# sql_query = """ CREATE TABLE IF NOT EXISTS School
# ( School_Id INTEGER NOT NULL PRIMARY KEY, School_Name TEXT NOT NULL,
# Place_Count INTEGER NOT NULL );"""
#
# sql_query1 = """
# INSERT INTO School (School_Id, School_Name, Place_Count)
# VALUES
# ('1', 'Протон', 200),
# ('2', 'Преспектива', 300),
# ('3', 'Спектр', 400),
# ('4', 'Содружество', 500);"""
#
# sql_query2 = """
# CREATE TABLE Teacher
# (Teacher_Id INTEGER NOT NULL PRIMARY KEY,
# Teacher_Name TEXT NOT NULL,
# School_Id INTEGER NOT NULL,
# Joining_Date TEXT NOT NULL,
# Speciality TEXT NOT NULL,
# Salary INTEGER NOT NULL,
# Experience INTEGER);"""
#
# sql_query3 = """
# INSERT INTO Teacher (Teacher_Id, Teacher_Name,
# School_Id, Joining_Date, Speciality, Salary, Experience)
# VALUES ('101', 'Галина', '1', '2021-2-10', 'Физик', '40000', NULL),
# ('102', 'Мария', '1', '2018-07-23', 'Химик', '20000', NULL),
# ('103', 'Ольга', '2', '2022-05-19', 'Информатик', '25000', NULL),
# ('104', 'Полина', '2', '2017-12-28', 'Физик ', '28000', NULL),
# ('105', 'Лидия', '3', '2015-06-04', 'Информатик', '42000', NULL),
# ('106', 'Анастасия', '3', '2019-09-11', 'Учитель трудов', '30000', NULL),
# ('107', 'Ирина', '4', '2020-08-21', 'Информатик', '32000', NULL),
# ('108', 'Виктория', '4', '2017-10-17', 'Географ', '30000', NULL);"""

# cursor.execute(sql_query3)
# connection.commit()

# задача №2 Подключиться к БД и вывести ее версию
#
# import sqlite3
# def get_connect():
#     connection = sqlite3.connect("teachers1.db")
#     return connection
#
#
# def close_connect(connection):
#     if connection:
#        connection.close()
#
# def task_2():
#     try:
#         con = get_connect()
#         cursor = con.cursor()
#         cursor.execute('SELECT sqlite_version();')
#         version = cursor.fetchone()
#         print ("вы подключились к версии", version)
#         close_connect(con)
#     except (Exception, sqlite3.Error) as error:
#         print ("Ошибка - ", error)

# task_2()



# задача №3 Заполнить колонку "опыт работы"

# import sqlite3
# def get_connect():
#     connection = sqlite3.connect("teachers1.db")
#     return connection
#
#
# def close_connect(connection):
#     if connection:
#        connection.close()
#
# def task_3():
#     try:
#         con = get_connect()
#         cursor = con.cursor()
#         cursor.execute("UPDATE Teacher set Experience = 2 WHERE School_ID=1")
#         cursor.execute("UPDATE Teacher set Experience = 5 WHERE School_ID=2")
#         cursor.execute("UPDATE Teacher set Experience = 8 WHERE School_ID=3")
#         cursor.execute("UPDATE Teacher set Experience = 10 WHERE School_ID=4")
#         con.commit()
#         close_connect(con)
#     except (Exception, sqlite3.Error) as error:
#         print ("Ошибка - ", error)
#
# task_3()


# задача №4 Вывод нужных данных по запросу ID школы и учителя

# import sqlite3
# def get_connect():
#     connection = sqlite3.connect("teachers1.db")
#     return connection
#
#
# def close_connect(connection):
#     if connection:
#        connection.close()
#
# def get_school_ID(school_ID):
#     try:
#         con = get_connect()
#         cursor = con.cursor()
#         sqlquery_n = 'SELECT * FROM school WHERE School_Id = ?'
#         cursor.execute(sqlquery_n, (school_ID,))
#         School_nn = cursor.fetchall()
#         print ('Данные по школе:')
#         for row in School_nn:
#             print("ID школы: ", row[0])
#             print("Название школы:", row[1])
#             print("Мест:", row[2],'\n')
#         close_connect(con)
#     except (Exception, sqlite3.Error) as error:
#         print("Ошибка - ", error)
#
# def teacher_ID(teach_ID):
#     try:
#         con = get_connect()
#         cursor = con.cursor()
#         sqlquery_n = 'SELECT * FROM Teacher WHERE Teacher_Id = ?'
#         cursor.execute(sqlquery_n, (teach_ID,))
#         teach_nn = cursor.fetchall()
#         print ('Данные по учителю:')
#         for row in teach_nn:
#             print("ID Учителя:: ", row[0])
#             print("Имя учителя:", row[1])
#             print("ID школы:", row[2])
#             print("Дата начала работы:", row[3])
#             print("Cпециализация:", row[4])
#             print("Зарплата:", row[5])
#             print("Опыт работы:", row[6])
#         close_connect(con)
#     except (Exception, sqlite3.Error) as error:
#         print("Ошибка - ", error)
#
#
#
# s = int(input ('Введи ID школы:'))
# t = int(input ('Введи ID учителя:'))
#
# get_school_ID(s)
# teacher_ID (t)

# задача №5 Вывести список учителей по заданной специальности и зарплате

# import sqlite3
# def get_connect():
#     connection = sqlite3.connect("teachers1.db")
#     return connection
#
#
# def close_connect(connection):
#     if connection:
#        connection.close()
#
# def teacher_detail(spec, sal):
#     try:
#         con = get_connect()
#         cursor = con.cursor()
#         sqlquery_n = 'SELECT * FROM Teacher WHERE speciality = ? AND salary > ?'
#         cursor.execute(sqlquery_n, (spec,sal))
#         teach_nn = cursor.fetchall()
#         print (f'Выборка по учителям: {spec} c зп больше {sal}')
#         for row in teach_nn:
#             print("ID Учителя:: ", row[0])
#             print("Имя учителя:", row[1])
#             print("ID школы:", row[2])
#             print("Дата начала работы:", row[3])
#             print("Cпециализация:", row[4])
#             print("Зарплата:", row[5])
#             print("Опыт работы:", row[6], '\n')
#         close_connect(con)
#     except (Exception, sqlite3.Error) as error:
#         print("Ошибка - ", error)
#
#
# # teacher_detail ('Информатик', 10000)
# teacher_detail ('Физик', 10000)


#задача №6 Вывести список учителей по ID школы (соединение информации из двух таблиц)

#Вар_1 Через две функции

import sqlite3
# def get_connect():
#     connection = sqlite3.connect("teachers1.db")
#     return connection
#
#
# def close_connect(connection):
#     if connection:
#        connection.close()
#
# def get_school_name(school_ID):
#     try:
#         con = get_connect()
#         cursor = con.cursor()
#         sqlquery_n = 'SELECT * FROM school WHERE School_Id = ?'
#         cursor.execute(sqlquery_n, (school_ID,))
#         School_nn = cursor.fetchone()
#         s_name = School_nn[1]
#         return s_name
#         close_connect(con)
#     except (Exception, sqlite3.Error) as error:
#         print("Ошибка - ", error)



# def teacher_ID_2(school_ID):
#     try:
#         con = get_connect()
#         cursor = con.cursor()
#         sqlquery_n = 'SELECT * FROM Teacher WHERE School_Id = ?'
#         cursor.execute(sqlquery_n, (school_ID,))
#         teach_nn = cursor.fetchall()
#         for row in teach_nn:
#             print("ID Учителя:: ", row[0])
#             print("Имя учителя:", row[1])
#             print("ID школы:", row[2])
#             print('Название школы:', get_school_name(row[2]))
#             print("Дата начала работы:", row[3])
#             print("Cпециализация:", row[4])
#             print("Зарплата:", row[5])
#             print("Опыт работы:", row[6], '\n')
#         close_connect(con)
#     except (Exception, sqlite3.Error) as error:
#         print("Ошибка - ", error)
#
# teacher_ID_2 (4)



# Вар.2 Через JOIN

# import sqlite3
# def get_connect():
#     connection = sqlite3.connect("teachers1.db")
#     return connection
#
# def close_connect(connection):
#     if connection:
#        connection.close()
#
# def teacher_ID_4(school_ID):
#     try:
#         con = get_connect()
#         cursor = con.cursor()
#         sqlquery_n = """SELECT * FROM Teacher JOIN School ON Teacher.School_Id = School.School_Id
#         WHERE School.School_Id = ?"""
#         cursor.execute(sqlquery_n, (school_ID,))
#         teach_nn = cursor.fetchall()
#         for row in teach_nn:
#             print("ID Учителя:: ", row[0])
#             print("Имя учителя:", row[1])
#             print("ID школы:", row[2])
#             print('Название школы:', row[8] )
#             print("Дата начала работы:", row[3])
#             print("Cпециализация:", row[4])
#             print("Зарплата:", row[5])
#             print("Опыт работы:", row[6], '\n')
#         close_connect(con)
#     except (Exception, sqlite3.Error) as error:
#         print("Ошибка - ", error)
#
# teacher_ID_4 (4)

#Вывод наименования таблиц

import sqlite3
# def get_connect():
#     connection = sqlite3.connect("teachers1.db")
#     return connection
#
#
# def close_connect(connection):
#     if connection:
#        connection.close()

# def table_name():
#     try:
#         con = get_connect()
#         cursor = con.cursor()
#         cursor.execute("""SELECT * FROM sqlite_master WHERE type = 'table';""")
#         tables = cursor.fetchall()
#         for t in tables:
#              # print (t) #Полная инфа о таблицах
#              print(t[1]) #Имена таблиц
#         close_connect(con)
#     except (Exception, sqlite3.Error) as error:
#         print ("Ошибка - ", error)
#
# table_name()


#Вывод наименования столбцов

import sqlite3
def get_connect():
    connection = sqlite3.connect("teachers1.db")
    return connection

def close_connect(connection):
    if connection:
       connection.close()

def column_name():
    try:
        con = get_connect()
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM Teacher""")
        colnames = cursor.description
        for n in colnames:
            print(n[0])
        close_connect(con)
    except (Exception, sqlite3.Error) as error:
        print ("Ошибка - ", error)

column_name()

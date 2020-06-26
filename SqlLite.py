# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:57:27 2020

@author: ARJUN
"""
import sqlite3
from random import randint
import datetime

__database__name__ = r"C:\sqlite\sqlite-tools-win32-x86-3320300\testdb"


class Sqllite3:
    def __init__(self):
        try:
            self.connection = sqlite3.connect(__database__name__)
            self.cur = self.connection.cursor()
        except Exception as e:
            print(f"Error connection: {e}")

    def __create__tables__(self):
        __create__table_query = """CREATE TABLE STUDENTMARKS(Rollnumber integer PRIMARY KEY, Name text NOT NULL, 
                                    Telugu integer NOT NULL, Hindi integer Not Null, English integer NOT NULL, 
                                    Maths integer NOT NULL, Science interger NOT NULL, Social integer NOT NULL)"""
        __create__table_user_credentials = "CREATE TABLE USERCREDENTIALS(username text PRIMARY KEY, password text NOT NULL)"
        __create__table_attendence = "Create Table studentattendence(username text, date text, present number)"
        __create__table_userinfo = "Create Table UserInfo(username text PRIMARY KEY, firstname text, lastname text, email text, gender text, dob text)"
        try:
            self.cur.execute(__create__table_query)
            self.cur.execute(__create__table_user_credentials)
            self.cur.execute(__create__table_attendence)
            self.cur.execute(__create__table_userinfo)
        except Exception as e:
            print(f"Error connection: {e}")

    def __check__table__existence__(self):
        __query = """SELECT name FROM sqlite_master WHERE type='table' AND name='STUDENTMARKS';"""
        self.cur.execute(__query)
        table = self.cur.fetchall()
        print(table)
        if len(table) == 0:
            self.__create__tables__()
        else:
            print(f"Table available: {table}")

    def __insert__students__marks__(self):
        __query = f"""Insert Into STUDENTMARKS(Name, Telugu, Hindi, English, Maths, Science, Social) 
        Values('{self.username}', {randint(50,100)}, {randint(50,100)}, {randint(50,100)}, {randint(50,100)}, {randint(50,100)}, {randint(50,100)})"""
        try:
            cur = self.connection.cursor()
            cur.execute(__query)
            self.connection.commit()
        except Exception as e:
            print(e)

    def __insert__userinfo__(self, data):
        __query = f"INSERT INTO  UserInfo(username, firstname, lastname, email, gender, dob) Values('{self.username}', '{data.get('firstname')}','{data.get('lastname')}','{data.get('email')}','{data.get('gender')}','{data.get('dob')}')"
        try:
            cur = self.connection.cursor()
            cur.execute(__query)
            self.connection.commit()
        except Exception as e:
            print(f"Error userinf: {e}")

    def __insert__attedence__(self):
        __query1 = f"""Insert Into studentattendence(username, date, present) Values('{self.username}', '{datetime.datetime(2019, 1, 30)}', {randint(20,26)})"""
        __query2 = f"""Insert Into studentattendence(username, date, present) Values('{self.username}', '{datetime.datetime(2019, 2, 27)}', {randint(20,26)})"""
        __query3 = f"""Insert Into studentattendence(username, date, present) Values('{self.username}', '{datetime.datetime(2019, 3, 30)}', {randint(20,26)})"""
        __query4 = f"""Insert Into studentattendence(username, date, present) Values('{self.username}', '{datetime.datetime(2019, 4, 30)}', {randint(20,26)})"""
        __query5 = f"""Insert Into studentattendence(username, date, present) Values('{self.username}', '{datetime.datetime(2019, 5, 30)}', {randint(20,26)})"""
        __query6 = f"""Insert Into studentattendence(username, date, present) Values('{self.username}', '{datetime.datetime(2019, 6, 30)}', {randint(20,26)})"""
        __query7 = f"""Insert Into studentattendence(username, date, present) Values('{self.username}', '{datetime.datetime(2019, 7, 30)}', {randint(20,26)})"""
        __query8 = f"""Insert Into studentattendence(username, date, present) Values('{self.username}', '{datetime.datetime(2019, 8, 30)}', {randint(20,26)})"""
        __query9 = f"""Insert Into studentattendence(username, date, present) Values('{self.username}', '{datetime.datetime(2019, 9, 30)}', {randint(20,26)})"""
        __query10 = f"""Insert Into studentattendence(username, date, present) Values('{self.username}', '{datetime.datetime(2019, 10, 30)}', {randint(20,26)})"""
        __query11 = f"""Insert Into studentattendence(username, date, present) Values('{self.username}', '{datetime.datetime(2019, 11, 30)}', {randint(20,26)})"""
        __query12 = f"""Insert Into studentattendence(username, date, present) Values('{self.username}', '{datetime.datetime(2019, 12, 30)}', {randint(20,26)})"""

        try:
            cur = self.connection.cursor()
            cur.execute(__query1)
            cur.execute(__query2)
            cur.execute(__query3)
            cur.execute(__query4)
            cur.execute(__query5)
            cur.execute(__query6)
            cur.execute(__query7)
            cur.execute(__query8)
            cur.execute(__query9)
            cur.execute(__query10)
            cur.execute(__query11)
            cur.execute(__query12)
            self.connection.commit()
        except Exception as e:
            print(e)

    def __is_username__available__(self, username):
        __select__query = f"SELECT username FROM USERCREDENTIALS WHERE username='{username}';"
        cur = self.connection.cursor()
        cur.execute(__select__query)
        name = cur.fetchone()
        print(name)
        if name is None:
            return True
        else:
            return False

    def __valid__credentials__(self, username, password):
        __select__query = f"SELECT username FROM USERCREDENTIALS WHERE username='{username}' and password='{password}';"
        cur = self.connection.cursor()
        cur.execute(__select__query)
        name = cur.fetchone()
        print(name)
        if name is None:
            return False
        else:
            return True

    def __insert__user__credentials__(self, username, password):
        self.username = username
        __insert__query = f"Insert Into USERCREDENTIALS(username, password) Values('{username}', '{password}')"
        cur = self.connection.cursor()
        cur.execute(__insert__query)
        self.connection.commit()

    def __get_marks__(self):
        __query = "SELECT * FROM STUDENTMARKS"
        try:
            cur = self.connection.cursor()
            cur.execute(__query)
            rows = cur.fetchall()
            print(rows)
        except Exception as e:
            print(e)

sl = Sqllite3()
s = sl.__is_username__available__("bharathn")
# s = sl.__check__table__existence__()
# sl.__insert__user__credentials__("sreekanthVENKATDVR", "bharath@123")
# sl.__insert__attedence__()
# sl.__insert__students__marks__()
# data = {"firstname":"bharath","lastname":"naidu","email":"bharathdbbara@gmail.com", "dob":"20/22/2","gender":"male"}
# sl.__insert__userinfo__(data)
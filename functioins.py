#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import pprint
import random
import pathlib


def inf():
    con = sqlite3.connect('mydatebase.db')
    file = pathlib.Path.cwd()/'inf.sql'
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read().split(';')
    cur= con.cursor()
    a = 0
    b = 1
    while a<b:
        a = random.randint(250, 300)
        b = random.randint(270, 300)
    cur.execute(data[7])
    fet = cur.fetchall()[-1:]
    c = fet[0][0]
    d = fet[0][1]
    cur.execute(data[6], (c, a, b, d))
    con.commit()
    con.close()


def selecting(nom=0):
    con = sqlite3.connect('mydatebase.db')
    file = pathlib.Path.cwd()/'inf.sql'
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read().split(';')
    cur= con.cursor()
    cur.execute(data[5], (nom,))
    pprint.pprint(cur.fetchall())
    con.close()


def table():
    con = sqlite3.connect('mydatebase.db')
    file = pathlib.Path.cwd()/'inf.sql'
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read().split(';')
    cur= con.cursor()
    print("\t\tТаблица рейсов")
    cur.execute(data[3])
    pprint.pprint(cur.fetchall())
    print("\t\tТаблица информации о самолёте")
    cur.execute(data[4])
    pprint.pprint(cur.fetchall())
    con.close()


def load():
    args = str(pathlib.Path.cwd() / "mydatebase.db")
    db_path = pathlib.Path(args)
    return db_path


def adding(file,stay="text", number="text", value="text"):
    con = sqlite3.connect(file)
    file = pathlib.Path.cwd()/'inf.sql'
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read().split(';')
    cur= con.cursor()
    cur.execute(data[2],(stay, number, value))
    con.commit()
    con.close()


def sql_connection():
    file = 'mydatebase.db'
    con = sqlite3.connect(file)
    con.close()
        

def sql_table():
    con = sqlite3.connect('mydatebase.db')
    file = pathlib.Path.cwd()/'inf.sql'
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read().split(';')
    cursor_obj = con.cursor()
    cursor_obj.execute(data[0])
    cursor_obj.execute(data[1])
    con.commit()
    con.close()

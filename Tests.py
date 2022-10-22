#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import functioins as fun
import tempfile
import shutil
from pathlib import Path
import sqlite3


class SqlTest(unittest.TestCase):
    """Тест операций по работе с SQL"""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path_dir = Path(self.tmp.name)
        shutil.copyfile(fun.load(), self.path_dir / 'test.db')
        self.fullpath = self.path_dir / 'test.db'
        self.conn = sqlite3.connect(self.fullpath)
        self.cursor = self.conn.cursor()
        self.file = Path.cwd()/'inf.sql'
        with open(self.file, 'r', encoding='utf-8') as f:
            data = f.read().split(';')
        self.data = data
        self.cursor.execute(self.data[3])
        self.rows = self.cursor.fetchall()
        self.result = [
            {
                "Место прибытия": row[1],
                "Номер самолёта": row[2],
                "Тип": row[3]
            }
            for row in self.rows
        ]

    def test_have_db(self):
        self.cursor.execute(self.data[8])
        table = self.cursor.fetchall()
        self.assertEqual(table, [('flights',), ('info',)])

    def test_add_shop(self):
        fun.adding(self.fullpath)
        self.cursor.execute(self.data[9])
        rows = self.cursor.fetchall()
        self.last = [
            {
                "Место прибытия": row[1],
                "Номер самолёта": row[2],
                "Тип": row[3]
            }
            for row in rows
        ]
        self.assertEqual(self.last, [{"Место прибытия": 'text', "Номер самолёта": 'text', "Тип": 'text'}])

    def test_select(self):
        self.assertListEqual(self.result, [{"Место прибытия": 'London', "Номер самолёта": 'RF-862112', "Тип": "Airbus"},
        {"Место прибытия": 'Moscow', "Номер самолёта": 'RF-85123', "Тип": "Boing"}])
    
    def tearDown(self):
        self.conn.close()
        self.tmp.cleanup()


if __name__ == '__main__':
    unittest.main()
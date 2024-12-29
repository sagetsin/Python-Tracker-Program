#!/usr/bin/env python

'''This is python sqlite3 database 
@author: Sydney Tsin
'''

import sqlite3

conn = sqlite3.connect('pas_database.db')
c = conn.cursor()

'''Create Table in Database'''
c.execute("""CREATE TABLE IF NOT EXISTS Materials 
          (p_id INTEGER PRIMARY KEY, idealNumber Integer, material TEXT, givenNumber INTEGER)""" )

'''Insert multiple rows of data into the table'''
MATERIALS = [(1, 90, 'Power', 0),
             (2, 20, 'Defense', 0),
             (3, 0, 'Mind', 0),
             (4, 0, 'Evade', 0),
             (5, 25, 'Luck', 0)]

c.executemany("""INSERT INTO Materials VALUES (?,?,?,?)""", MATERIALS)

conn.commit()
conn.close()
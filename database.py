#!.\venv\Scripts\python.exe
'''This is python sqlite3 database 
@author: Sydney Tsin
'''

import sqlite3

conn = sqlite3.connect('pas_database.db')
c = conn.cursor()

'''Create Table in Database'''
c.execute("""CREATE TABLE IF NOT EXISTS Materials 
          (p_id INTEGER PRIMARY KEY, idealNumber Integer, material TEXT, givenNumber INTEGER)""" )

conn.commit()
conn.close()
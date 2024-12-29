#!/usr/bin/env python
'''Tracker file to modify and updtate the database
@author: Sydney Tsin
'''
import sqlite3

conn = sqlite3.connect('pas_database.db')
c = conn.cursor()

'''Display table in relational database'''
def print_table(table):
    print(table) #Prints table header
    for row in c.execute("""SELECT * FROM """ + table):
        print(row)

print_table('Materials')
conn.close()


#!/usr/bin/env python
'''Tracker file to modify and updtate the database
@author: Sydney Tsin
'''

from subprocess import call
import sys
import sqlite3

conn = sqlite3.connect('pas_database.db')
c = conn.cursor()

'''Display table in relational database'''
def print_table(table):
    print('/-----------------------------------------\\')
    print(table + '\n-----------------') #Prints table header
    for row in c.execute("""SELECT * FROM """ + table):
        print(row)
    print('\\-----------------------------------------/')

'''Function to display add/edit menu'''
def add_edit_menu():
    call('clear')
    print_table('Materials')
    print('\\-----------------------------------------/')
    print('e). Exit\n')

'''Function for adding material'''
def add_material(choice):
    c.execute("""UPDATE Materials SET givenNumber = givenNumber + 1 WHERE p_id = ?""", (int(choice),))
    conn.commit()

'''Function for editing material'''
def edit_material(choice, value):
    c.execute("""UPDATE Materials SET givenNumber = ? WHERE p_id = ?""", (int(value), int(choice),))
    conn.commit()

'''Function for deleting a single material'''
def remove_material(choice):
    c.execute("""UPDATE Materials SET givenNumber = givenNumber - 1 WHERE p_id = ?""", (int(choice),))
    conn.commit()

'''Function for deleting all of one material'''
def clear_material(choice):
    c.execute("""UPDATE Materials SET givenNumber = 0 WHERE p_id = ?""", (int(choice),))
    conn.commit()

'''Function for clearing all materials in the table'''
def clear_table():
    id_arr = [0] * 6
    for id in c.execute("""SELECT p_id FROM Materials"""):
        id_arr[id[0]] = id[0]
    for i in id_arr:
        clear_material(i)
    conn.commit()

'''define Menu 1'''
def menu_1():
    print('\nMenu')
    print('1). Add Material')
    print('2). Edit Material')
    print('3). Remove Material')
    print('4). Reset Material')
    print('5). Reset all Materials')
    print('e). Exit\n')

'''Feedback function to let user know the changes have been made'''
def feedback(number):
    c.execute("""SELECT material, givenNumber FROM Materials WHERE p_id = ?""", (int(number),))
    data = c.fetchone()
    print(f'{data[0]} material has been changed to {data[1]}\n')


call('clear')
print_table('Materials')
menu_1()
choice = input("How can I help you today? ")
while(choice >= '1' and choice <= '5'):
    if choice =='1':
        add_edit_menu()
        add_choice = input("What material would you like to add? ")
        if add_choice >= '1' and add_choice <= '5':
            add_material(add_choice)
            call('clear')
            feedback(add_choice)
        else:
            print("Invalid choice. Exiting...")
            sys.exit()
    elif choice == '2':
        add_edit_menu()
        edit_choice = input("What material would you like to edit? ")
        if edit_choice >= '1' and edit_choice <= '5':
            value = input("Please provide a new value for this Material: ")
            edit_material(edit_choice, value)
            call('clear')
            feedback(edit_choice)
        else:
            print("Invalid choice. Exiting...")
            sys.exit()
    elif choice == '3':
        add_edit_menu()
        remove_choice = input("What material would you like to remove from? ")
        if remove_choice >= '1' and remove_choice <= '5':
            remove_material(remove_choice)
            call('clear')
            feedback(remove_choice)
        else:
            print("Invalid choice. Exiting...")
            sys.exit()
    elif choice == '4':
        add_edit_menu()
        reset_choice = input("What material would you like to reset? ")
        if reset_choice >= '1' and reset_choice <= '5':
            clear_material(reset_choice)
            call('clear')
            feedback(reset_choice)
        else:
            print("Invalid choice. Exiting...")
            sys.exit()
    elif choice == '5':
        clear_table()
        call('clear')
        print("All Materials have be reset to 0")
    print_table('Materials')
    menu_1()
    choice = input("How can I help you today? ")
print("Exiting...")
sys.exit()


conn.close()


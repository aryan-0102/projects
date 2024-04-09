#!/usr/bin/env python3
import mysql.connector
import time
import pyfiglet

from google.cloud import storage 
from datetime import datetime
import sys
 
T = "Hostel Management System 1.0 "
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)
print("""
-----------------------------------------------------
-----------------------------------------------------

MIT License:
This software is licensed under the MIT License.

Developed by:
Aryan Dhasmana, Nikhil Gusain, Simranjeet Kaur,
Aseem Kamboj, Atharv Pratap Singh Chundawat

Powered by PyFiglet, MySQL 8.0.3, and Python 3.10.12.
""")

mycon = mysql.connector.connect(user='me', password='aryan', host='34.170.231.29', database='db')
cursor = mycon.cursor()
if mycon.is_connected() == False:
    print('con fail')


# --------------------FUNCTIONS--------------------
#-------- sleep --------- 

def sleep():
    for i in range(3):
        time.sleep(1)
        print('.\n.\n.')
        i += 1
        print('Wait\n')

# -------------- Delete -------------

def delete():
    adm = input('Enter admission number : ')
    st = ('delete from student where adm = %s ',(adm,))
    cursor.execute(st)
    mycon.commit()
# --------------------new warden -------------------
def wardadd():
    name = input('Enter Name: ')
    empid = input('Enter Employee ID: ')
    contact = input('Enter Contact: ')
    passwd = input('Enter password: ')
    passconf = input('Confirm Password: ')
    
    while passwd != passconf:
        print('Password not matching. Try Again!')
        passconf = input('Confirm Password: ')

    st = "INSERT INTO warden (name, empid, contact, passwd) VALUES (%s, %s, %s, %s)"
    values = (name, empid, contact, passwd)
    cursor.execute(st, values)
    mycon.commit()
    sleep()
    print('New ward added successfully!')

    return


# --------------------------------------------add student--------------------------------------------

def addstu():
    name = input('Enter Name: ')
    contact = input('Enter Contact: ')
    address = input('Enter Address: ')
    adm = input('Enter Admission No.: ')
    h_name = input('Enter Hostel Name: ')
    rm_no = input('Enter Room No: ')

    # Insert student details into the database
    st = f"INSERT INTO student (name, contact, Address, adm, h_name, Rm_no) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (name,contact,address,adm,h_name,rm_no)
    cursor.execute(st, values)
    # Commit the transaction
    mycon.commit()
    sleep() 
    print("\nStudent details added successfully......")

    return

# --------------------------------------------fee calculator--------------------------------------------

def calcfee():
    num = input('Enter Admission number: ')
    st = 'SELECT fee, fine FROM student WHERE adm = %s'
    cursor.execute(st, (num,))
    result = cursor.fetchone()  
    if result:
        fee, fine = result
        total = int(fee) + int(fine)
        print('Total Dues:', total)
        if total == 0 :
            print('No dues ...')
            return
        else :
            dec = input('PAY DUE FEE Y/N : ')
            deci = dec.lower()
            if deci == 'y':
                st = 'UPDATE student SET fee = 0, fine = 0 WHERE adm = %s'
                cursor.execute(st, (num,))
                sleep()
                print('All dues cleared Successfully.....')
                mycon.commit()

            else:
                return

    else:
        print('Student not found.')
        return None

# ------------------------- - Fee payment --------------------------
''' def payfee(adm):
    st = 'UPDATE student SET fee = 0, fine = 0 WHERE adm = %s'
    cursor.execute(st, (adm,))
    sleep()
    print('All dues cleared Successfully.....')
    mycon.commit()  '''
# --------------------------------------------guest entry--------------------------------------------

def guest():
    nam = str(input('Enter Name :'))
    con = str(input('Enter Contact :'))
    stu = input('Enter Student Name : ')
    roomno = input('Enter Room No : ')
    rel = input('Enter Relation : ')
    cursor.execute(f'INSERT INTO guest(name,contact,student,room_no,relation) Values(\"{nam}\",{con},\"{stu}\",{roomno},\"{rel}\")')
    mycon.commit()
    sleep()
    print('Updated Successfully ..... \n\n')


# --------------------------------------------login--------------------------------------------
def log():
    attempts = 0  # Counter for login attempts
    
    while attempts < 3:
        empid = input('Enter Employee ID : ')
        passwd = input('Enter Password : ')

        st = "SELECT passwd FROM warden WHERE empid = %s"
        cursor.execute(st, (empid,))
        data = cursor.fetchone()

        if data:  # Check if data is not empty
            stored_passwd = data[0]  # Assuming the password is stored in the first column
            if passwd == stored_passwd:
                print('Login successful!..........\n')
                break  # Exit the loop if login is successful
            else:
                print('Login failed. Incorrect password.')
        else:
            print('ERROR.....Employee ID not found.....')
            print('Contact Administration for assistance.\n')
        attempts += 1  # Increment attempts counter

    if attempts == 3:
        print('\n\n....Maximum login attempts reached. Contact Admin to reset password.\n Exiting...\n\n')
        exit()  # Exit the program after maximum attempts reached

 # -------------------------------------------Retrieving hostel data -------------------------------------------
def hostel_data():
    print('Hostels Available: ')
    print('1.ARAVALI')
    print('2.HIMALAYA')
    print('3.SHIVALIK')
    print('4.NILGIRI')
    hostel = ''
    hos = int(input('Choose Hostel : '))
    if hos == 1:
        hostel = 'aravali'
    elif hos == 2:
        hostel = 'himalaya'
    elif hos == 3:
        hostel = 'shivalik'
    elif hos == 4:
        hostel = 'nilgiri'
    print(f'\n\n {hostel}\n')
    cursor.execute(f'Select name, Rm_no, contact from student where h_name = \'{hostel}\'')
    da = cursor.fetchall()
    for i in da :
        print(i)


# -------------------------------------------Retrieving data -------------------------------------------

def data():
    adm = input('Enter Student Adm No. :')
    st = f'select * from student where adm={adm}'
    cursor.execute(st)
    dat = cursor.fetchall()
    sleep()
    print(dat)



# ---------------------------------------------------END FUNCTIONS---------------------------------------------------
# --------------------------------------------------------------------------------------------------------------

# ---------------------LogIN-------------------

print('**  LOGIN  **')

log()

# main program
while True:
    print('')
    print('\n\n\"HOSTEL MANAGEMENT SYSTEM\"\n')

    print('')
    print('1. Guest Entry')
    print('2. General Operations')
    print('3. Exit\n')
    choice = int(input('Preferred operation : '))
    if choice == 1:
        guest()
    elif choice == 2:
        print('\n\nAvailable Operations : ')
        print('')
        print('1. View Student Details')
        print('2. Fee payment')
        print('3. Add New Student')
        print('4. Add New Warden ')
        print('5. Get Hostel Detail')
        print('6. Delete student ')
        op = int(input('\nPreferred operation : '))
        if op == 1:
            data()
        elif op == 2:
            calcfee()
        elif op == 3:
            addstu()
        elif op == 4:
            wardadd()
        elif op == 5:
            hostel_data()
        elif op == 6:
            delete()
    elif choice == 3:
        print('Exiting program.......')
        time.sleep(2)
        mycon.commit()
        exit()
        print('Invalid Choice ')
        break

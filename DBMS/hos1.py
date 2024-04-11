#!/usr/bin/env python3
import mysql.connector
import time
import pyfiglet
import typer
from rich.progress import Progress, SpinnerColumn, TextColumn, track
from rich.console import Console
from rich import print
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import time
from prettytable import PrettyTable


from rich.live import Live
from rich.table import Table


T = "Hostel Management System 1.0 "
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)
print("""
-----------------------------------------------------
-----------------------------------------------------

MIT License:
This software is licensed under the MIT License.

Developed by:
Aryan Dhasmana, Nikhil Gusain, Simranjit Kaur,
Aseem Kamboj, Atharva Pratap Singh Chundawat

Powered by PyFiglet, MySQL 8.0.3, and Python 3.10.12.
""")

mycon = mysql.connector.connect(host='localhost', user='root', passwd='password', database='hms')
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
def payfee(adm):
    st = 'UPDATE student SET fee = 0, fine = 0 WHERE adm = %s'
    cursor.execute(st, (adm,))
    sleep()
    print('All dues cleared Successfully.....')
    mycon.commit()  
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
        progress('Validitating ....')

        st = "SELECT passwd FROM warden WHERE empid = %s"
        cursor.execute(st, (empid,))
        data = cursor.fetchone()

        if data:  # Check if data is not empty
            stored_passwd = data[0]  
            if passwd == stored_passwd:
                print('[bold blue]Login successful!..........[/bold blue]\n')
                break  # Exit the loop if login is successful
            else:
                print("[bold red]Alert![/bold red] Login failed. Incorrect password.")
        else:
            print('[bold red]ERROR[/bold red].....Employee ID not found.....')
            print('[bold green]Contact Administration for assistance.[/bold green]\n')
        attempts += 1  # Increment attempts counter

    if attempts == 3:
        print('\n\n[bold red]....Maximum login attempts reached.[/bold red] Contact Admin to reset password.\n Exiting...\n\n')
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
    dat = cursor.fetchone()
    print('\n')
    progress("Fetching data ....")

    print(dat)



# ---------------------------------------------------END FUNCTIONS---------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
def progress(str):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description=str, total=None)
        time.sleep(5)
    print("Done!")

def bar():
    total = 0
    for value in track(range(100), description="Processing..."):
        # Fake processing time
        time.sleep(0.02)
        total += 1
    print(f"Processed {total} things.")


# ===========================================================================================================================
# ===========================================================================================================================


def main():
    log()
    print('\n')
    action = inquirer.select(
        message="Select an action:",
        choices=[
            "Guest Entry",
            "General Operations",
            Choice(value=None, name="Exit"),
        ],
        default=None,
    ).execute()
    if action == 'Guest Entry':
        guest()
    elif action == 'General Operations' :
        action = inquirer.select(
            message = "Select An Operation : ",
            choices =[ 
                "1. Add Warden ",
                "2. View Student Details",
                "3. Fee Payment",
                "4. Add New Student",
                "5. Get Hostel Detail",
                "6. Delete Student",
                Choice(value=None , name="Exit"),
            ],
            default =None,
        ).execute()
        if action =="1. Add Warden " :
            wardadd()
        elif action =="2. View Student Details":
            data()
        elif action =="3. Fee Payment":
            calcfee()
        elif action =="4. Add New Student":
            addstu()
        elif action =="5. Get Hostel Detail":
            hostel_data()
        elif action =="6. Delete Student":
            delete()

    elif action == "Exit" :
        total = 0
        for value in track(range(100), description="Exiting..."):
        # Fake processing time
            time.sleep(0.02)
            total += 1
        exit()

       
if __name__ == "__main__":
    typer.run(main)
    while():
        main()
    

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
import sys
import random
import os
from rich.live import Live
from rich.table import Table


T = "Hostel Management System 1.0 "
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)
print("""
-----------------------------------------------------
-----------------------------------------------------

[bold]MIT License:
This software is licensed under the MIT License.

Developed by:
Aryan Dhasmana, Nikhil Gusain, Simranjeet Kaur,
Aseem Kamboj, Atharv Pratap Singh Chundawat

Powered by PyFiglet, MySQL 8.0.3, and Python 3.10.12.
      \n\n[/bold]
""")

mycon = mysql.connector.connect(host='localhost', user='root', passwd='password', database='hms')
cursor = mycon.cursor()
if mycon.is_connected() == False:
    print('con fail')


# --------------------FUNCTIONS--------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#-------------------- Hostel Menu ------------
def generate_hostel_menu():
    title = pyfiglet.figlet_format("Hostel Options")
    table_header = "| Hostel    | Monthly Fee (INR) | Facilities        | No. of People     |\n"
    separator = "|-----------|--------------------|-------------------|--------------------|\n"
    hostel_data = [
        "| Himalaya  |       140,000      | Air Conditioned   |    Two-seater      |\n",
        "| Nilgiri   |       110,000      | Coolers           |    Two-seater      |\n",
        "| Shivalik  |       120,000      | Air Conditioned   |    Three-seater    |\n",
        "| Aravali   |       100,000      | Coolers           |    Four-seater     |\n"
    ]

    hostel_menu = title + "\n" + table_header + separator
    for line in hostel_data:
        hostel_menu += line
    hostel_menu += separator

    return hostel_menu

# ========================= Mess Menu =======================
def generate_mess_menu():
    title = pyfiglet.figlet_format("Mess Options")
    table_header = "| Mess              | Monthly Fee (INR) | Type        |\n"
    separator = "|-------------------|--------------------|-------------|\n"
    mess_data = [
        "| North Indian Veg  |        5,000       | Veg         |\n",
        "| North Indian Non-Veg|      8,000       | Non-Veg     |\n",
        "| South Indian Veg  |        5,000       | Veg         |\n",
        "| South Indian Non-Veg|      8,000       | Non-Veg     |\n"
    ]

    mess_menu = title + "\n" + table_header + separator
    for line in mess_data:
        mess_menu += line
    mess_menu += separator

    return mess_menu
#-------- sleep --------- 

def sleep():
    for i in range(3):
        time.sleep(1)
        print('.\n.\n.')
        i += 1
        print('Wait\n')

# -------------- Delete -------------



'''def delete():
    adm = input('Enter admission number : ')
    st = f"SELECT * FROM student WHERE adm = '{adm}'"
    cursor.execute(st)
    result = cursor.fetchone()

    if result:
        fee = result[6]  # Index 6 represents the fee column
        fine = result[7]  # Index 7 represents the fine column

        if fee == 0 and fine == 0:
            progress('Processing')

            print(f'\n[bold green]Successfully Deleted Record for Admission number {adm}[/bold green]')
            table = PrettyTable()
            table.field_names = [i[0] for i in cursor.description]  # Get column names
            table.add_row(result)  # Add the fetched row to the table
            print("Student Record:")
            print(table)

            str = f"DELETE FROM student WHERE adm = '{adm}'"
            cursor.execute(str)
            mycon.commit()
        else:
            print("[bold red]Cannot delete student. Pending Dues....[/bold red]")
    else:
        print('[bold red]Student not found.[/bold red]')'''
def delete():
    adm = input('Enter admission number : ')
    st = f"SELECT * FROM student WHERE adm = '{adm}'"
    cursor.execute(st)
    result = cursor.fetchone()

    if result:
        fee = result[6]  # Index 6 represents the fee column
        fine = result[7]  # Index 7 represents the fine column
        total = fee + fine
        if fee == 0 and fine == 0:
            progress('Processing')

            print(f'\n[bold green]Successfully Deleted Record for Admission number {adm}[/bold green]')
            table = PrettyTable()
            table.field_names = [i[0] for i in cursor.description]  # Get column names
            table.add_row(result)  # Add the fetched row to the table
            print("Student Record:")
            print(table)

            str = f"DELETE FROM student WHERE adm = '{adm}'"
            cursor.execute(str)
            mycon.commit()
        else:
            print("[bold red]Cannot delete student. Pending Dues....[/bold red]")
            action = inquirer.select(
                message="PAY DUES ? ",
                choices=["Yes", "No"],
                default=None,
            ).execute()

            if action == "Yes":
                print(f'Total Dues = {total}\n')
                str = f"UPDATE student SET fee = 0, fine = 0 WHERE adm = '{adm}'"
                cursor.execute(str)
                mycon.commit()
                progress('Processing')

                
                st = f"SELECT * FROM student WHERE adm = '{adm}'"
                cursor.execute(st)
                result = cursor.fetchone()
                print(f'\n[bold green]Successfully Deleted Record for Admission number {adm}[/bold green]')
                table = PrettyTable()
                table.field_names = [i[0] for i in cursor.description]  # Get column names
                table.add_row(result)  # Add the fetched row to the table
                print("Student Record:")
                print(table)

                str = f"DELETE FROM student WHERE adm = '{adm}'"
                cursor.execute(str)
                mycon.commit()

                
            else:
                print("[bold yellow]Deletion canceled.[/bold yellow]")
    else:
        print('[bold red]Student not found.[/bold red]')



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
    progress('Processing request....')
    print('[bold green]New ward added successfully![/bold green]')

    return


# --------------------------------------------add student--------------------------------------------
'''
def addstu():
    name = input('Enter Name: ')
    contact = input('Enter Contact: ')
    address = input('Enter Address: ')
    adm = input('Enter Admission No.: ')
    gender = input('Enter Gender (Male/Female): ')
    print(generate_mess_menu())
    # Prompt user to select mess type
    mess_type = inquirer.select(
        message="Select Mess Type:",
        choices=["North Indian (Veg)", "North Indian (Non-Veg)", "South Indian (Veg)", "South Indian (Non-Veg)", Choice(value='Exit', name="Exit")],
        default=None,
    ).execute()
    
    if mess_type == "Exit":
        return
    
    # Set fee based on mess type and sub-option
    if "Veg" in mess_type:
        fee = 5000
    else:
        fee = 8000
    print(generate_hostel_menu())
    action = inquirer.select(
        message="Select Hostel:",
        choices=["Aravali", "Himalaya", "Shivalik", "Nilgiri", Choice(value='Exit', name="Exit")],
        default=None,
    ).execute()
    
    if action == "Exit":
        return
    
    h_name = action
    rm_no = random.randint(100, 700)

    # Insert student details into the database
    st = "INSERT INTO student (name, contact, Address, adm, gender, mess_type, fee, h_name, Rm_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (name, contact, address, adm, gender, mess_type, fee, h_name, rm_no)
    cursor.execute(st, values)
    
    # Commit the transaction
    mycon.commit()
    progress("Processing Data")
    print("\n[bold green]Student details added successfully......[/bold green]")
    print(f'Room no. {rm_no} assigned.')
'''
def addstu():
    name = input('Enter Name: ')
    contact = input('Enter Contact: ')
    address = input('Enter Address: ')
    adm = input('Enter Admission No.: ')
    gender = input('Enter Gender (Male/Female): ')
    clear_screen()
    print(generate_mess_menu())
    # Prompt user to select mess type
    mess_type = inquirer.select(
        message="Select Mess Type:",
        choices=["North Indian (Veg)", "North Indian (Non-Veg)", "South Indian (Veg)", "South Indian (Non-Veg)", Choice(value='Exit', name="Exit")],
        default=None,
    ).execute()
    
    if mess_type == "Exit":
        return
    
    # Set fee based on mess type and sub-option
    if "Veg" in mess_type:
        fee = 5000
    else:
        fee = 8000
    clear_screen()
    print(generate_hostel_menu())
    # Prompt user to select hostel
    action = inquirer.select(
        message="Select Hostel:",
        choices=["Aravali", "Himalaya", "Shivalik", "Nilgiri", Choice(value='Exit', name="Exit")],
        default=None,
    ).execute()
    
    if action == "Exit":
        return
    
    h_name = action
    rm_no = random.randint(100, 700)

    # Update fee for hostel using set_fee function
    if h_name == "Himalaya":
        fee = fee + 140000
    elif h_name == "Nilgiri":
        fee = fee + 110000
    elif h_name == "Shivalik":
        fee =fee + 120000
    elif h_name == "Aravali":
        fee = fee+ 100000
    
    # Insert student details into the database
    st = "INSERT INTO student (name, contact, Address, adm, gender, mess_type, fee, h_name, Rm_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (name, contact, address, adm, gender, mess_type, fee, h_name, rm_no)
    cursor.execute(st, values)
    
    # Commit the transaction
    mycon.commit()
    
    # Confirmation message with total fee and details
    total_fee = fee
    confirmation_message = f"\n[bold green]Student details added successfully......[/bold green]\n"
    confirmation_message += f"Name: {name}\n"
    confirmation_message += f"Contact: {contact}\n"
    confirmation_message += f"Address: {address}\n"
    confirmation_message += f"Admission No.: {adm}\n"
    confirmation_message += f"Gender: {gender}\n"
    confirmation_message += f"Mess Type: {mess_type}\n"
    confirmation_message += f"Hostel: {h_name}\n"
    confirmation_message += f"Room No.: {rm_no}\n"
    confirmation_message += f"Total Fee: {total_fee}\n"
    
    print(confirmation_message)
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
            print('[bold blue]No dues ...[/bold blue]')
            return
        else :
            dec = input('PAY DUE FEE Y/N : ')
            deci = dec.lower()
            if deci == 'y':
                st = 'UPDATE student SET fee = 0, fine = 0 WHERE adm = %s'
                cursor.execute(st, (num,))
                progress('Processing Transaction')
                print('[bold green]All dues cleared Successfully.....[/bold green]')
                mycon.commit()

            else:
                return

    else:
        print('[bold red]Student not found.[/bold red]')
        return None

# ------------------------- - Fee payment --------------------------
def payfee(adm):
    st = 'UPDATE student SET fee = 0, fine = 0 WHERE adm = %s'
    cursor.execute(st, (adm,))
    progress("Working .... ")
    print('[bold green]All dues cleared Successfully.....[/bold green]')
    mycon.commit()  


# ---------------------------------------------Set fee-----------------------------------
def set_fee():
    adm = input('Enter admission number: ')
    
    select_query = 'SELECT fee, fine FROM student WHERE adm = %s'
    cursor.execute(select_query, (adm,))
    result = cursor.fetchone()
    
    if result:
        fee, fine = result
        print(f'Current Fee: {fee}')
        print(f'Current Fine: {fine}')
        
        new_fee = input('Enter new fee: ')
        
        update_query = 'UPDATE student SET fee = %s WHERE adm = %s'
        cursor.execute(update_query, (new_fee, adm))
        mycon.commit()
        
        print('[bold green]Fee updated successfully![/bold green]')
    else:
        print('[bold red]Student not found.[/bold red]')

# --------------------------------------------guest entry--------------------------------------------

def guest():
    nam = str(input('Enter Name :'))
    con = str(input('Enter Contact :'))
    stu = input('Enter Student Name : ')
    roomno = input('Enter Room No : ')
    rel = input('Enter Relation : ')
    time = input('Enter entry time : ')
    cursor.execute(f'INSERT INTO guest(name,contact,student,room_no,relation,time) Values(\"{nam}\",{con},\"{stu}\",{roomno},\"{rel}\",{time})')
    mycon.commit()
    progress("Working")

    print('[bold green]Updated Successfully ..... \n\n[/bold green]')


def print_recent_guests():
    try:
        # Execute SQL query to retrieve 5 most recent guest records
        query = "SELECT * FROM guest ORDER BY time DESC LIMIT 5"
        cursor.execute(query)
        guests = cursor.fetchall()

        if guests:
            print("[bold underline]Recent Guest Records:[/bold underline]")

            table = PrettyTable()


            table.field_names = ["Name", "Contact", "Student", "Room No", "Relation", "Entry Time"]


            for guest in guests:
                table.add_row([guest[0], guest[1], guest[2], guest[3], guest[4], guest[5]])


            print(table)
        else:
            print("[bold red]No guest records found.[/bold red]")
    except mysql.connector.Error as err:
        print(f"[bold red]Error while retrieving guest records: {err}[/bold red]")


# --------------------------------------------login--------------------------------------------

def log():

    print("[bold red]**** LOGIN ****[/bold red]")
    attempts = 0  # Counter for login attempts
    
    while attempts < 3:
        empid = input('Enter Employee ID : ')
        passwd = inquirer.secret(message="Password:").execute()
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
'''def hostel_data():
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
        print(i)'''

def hostel_data():
    '''print('Hostels Available:')
    print('1. ARAVALI')
    print('2. HIMALAYA')
    print('3. SHIVALIK')
    print('4. NILGIRI')'''

    action = inquirer.select(
            message="Select an Hostel:",
            choices=[
                "Aravali",
                "Himalaya",
                "Shivalik",
                "Nilgiri",
                Choice(value='Exit', name="Exit"),
            ],
            default=None,
        ).execute()

    if action != "Exit":
        hostel = action ;
    
    print(f'\n{hostel.capitalize()}\n')

    cursor.execute(f'SELECT name, Rm_no, contact FROM student WHERE h_name = \'{hostel}\'')
    data = cursor.fetchall()
    
    if data:
        table = PrettyTable(['Name', 'Room No', 'Contact'])
        table.align['Name'] = 'l'
        table.align['Room No'] = 'r'
        table.align['Contact'] = 'r'
        for row in data:
            table.add_row(row)
        print(table)
    else:
        print("[bold red]No students found in this hostel.[/bold red]")

# -------------------------------------------Retrieving data -------------------------------------------

def data():
    adm = input('Enter Student Adm No. :')
    st = f'select * from student where adm={adm}'
    cursor.execute(st)
    
    rows = cursor.fetchall()
    if rows:
# Get column names
        columns = [i[0] for i in cursor.description]

# Create a PrettyTable object
        table = PrettyTable(columns)

# Add rows to the table
        for row in rows:
            table.add_row(row)

# Print the table
        print(table)
        '''
        dat = cursor.fetchone()
        print('\n')
        progress("Fetching data ....")

        print(dat)'''

    else:
        print('[bold red]Student not found.[/bold red]')

# ---------------------------------------------------END FUNCTIONS---------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
def progress(str):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description=str, total=None)
        time.sleep(3)
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


def train():
    log()
    while True :
        print('\n')
        action = inquirer.select(
            message="Select an action:",
            choices=[
                "Guest Entry",
                "General Operations",
                "Recent Guests",
                Choice(value='Exit', name="Exit"),
            ],
            default=None,
        ).execute()
        
        if action == 'Guest Entry':
            guest()
        elif action == "Recent Guests":
            print_recent_guests()
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
                    "7. Set Fee",
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
            elif action =="7. Set Fee":
                set_fee()

        elif action == "Exit" :
            total = 0
            for value in track(range(100), description="Saving Data..."):
        # Fake processing time
                time.sleep(0.02)
                total += 1
            raise typer.Exit()
            

       
if __name__ == "__main__":
    typer.run(train)
    raise typer.Exit()
    

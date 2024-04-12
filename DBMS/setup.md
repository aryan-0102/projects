# Setting up the Database

## Introduction

This document provides instructions for setting up the database required for the Hostel Management System.

## Instructions

1. **Download Scripts**: 
    - Download the `create_database.sh` and `create_tables.sql` files from the repository.

2. **Provide MySQL Credentials**:
    - Open the `create_database.sh` file in a text editor.
    - Replace `"your_mysql_username"` and `"your_mysql_password"` with your MySQL username and password.

3. **Save the Changes**:
    - Save the `create_database.sh` file after making the necessary changes.

4. **Make Shell Script Executable**:
    - Open a terminal.
    - Navigate to the directory containing the `create_database.sh` file.
    - Run the following command to make the shell script executable:
        ```bash
        chmod +x create_database.sh
        ```

5. **Execute Shell Script**:
    - Run the following command in the terminal to execute the shell script and create the database and tables:
        ```bash
        ./create_database.sh
        ```

6. **Verify Database Creation**:
    - After executing the shell script, verify that the database and tables have been created successfully in your MySQL environment.

7. **Database Setup Complete**:
    - Once the database and tables have been created successfully, the setup process is complete.

## Database Creation Script

Create a shell script named `create_database.sh` with the following content:

```bash
#!/bin/bash

# MySQL Connection Details
MYSQL_USER="your_mysql_username"
MYSQL_PASSWORD="your_mysql_password"

# SQL Script File
SQL_SCRIPT="create_tables.sql"

# Check if MySQL credentials are provided
if [ -z "$MYSQL_USER" ] || [ -z "$MYSQL_PASSWORD" ]; then
    echo "MySQL username or password not provided. Please set MYSQL_USER and MYSQL_PASSWORD variables."
    exit 1
fi

# Check if the SQL script file exists
if [ ! -f "$SQL_SCRIPT" ]; then
    echo "SQL script file '$SQL_SCRIPT' not found."
    exit 1
fi

# Execute SQL script using MySQL command-line tool
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" < "$SQL_SCRIPT"

# Check if MySQL command was successful
if [ $? -eq 0 ]; then
    echo "Database and tables created successfully."
else
    echo "Error: Failed to create database and tables."
fi
```

# SQL Script for Database Creation

```sql
CREATE DATABASE IF NOT EXISTS hms;

USE hms;

CREATE TABLE IF NOT EXISTS guest (
    name VARCHAR(255) NOT NULL,
    contact VARCHAR(20) NOT NULL PRIMARY KEY,
    student VARCHAR(255),
    room_no INT,
    relation VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS student (
    name VARCHAR(255) NOT NULL,
    contact VARCHAR(255),
    Address VARCHAR(255),
    adm INT NOT NULL PRIMARY KEY,
    h_name VARCHAR(255),
    Rm_no INT,
    fee INT DEFAULT 0,
    fine INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS warden (
    name VARCHAR(40),
    empid INT NOT NULL PRIMARY KEY,
    contact INT,
    passwd VARCHAR(255) NOT NULL DEFAULT 'pass'
);



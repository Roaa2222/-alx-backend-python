#!/usr/bin/env python3
import mysql.connector
import csv
import uuid
import os


def connect_db():
    """Connect to MySQL server (without selecting database)."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",         # Replace with your MySQL username
            password="root"      # Replace with your MySQL password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_database(connection):
    """Create the ALX_prodev database if it doesn't exist."""
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    cursor.close()


def connect_to_prodev():
    """Connect to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_table(connection):
    """Create the user_data table if it doesn't exist."""
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX (user_id)
        );
    """)
    connection.commit()
    print("Table user_data created successfully")
    cursor.close()


def insert_data(connection, csv_file):
    """Insert data from CSV into user_data table if not already present."""
    cursor = connection.cursor()

    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user_id = row['user_id']
            name = row['name']
            email = row['email']
            age = row['age']

            cursor.execute("SELECT user_id FROM user_data WHERE user_id = %s", (user_id,))
            if cursor.fetchone() is None:
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, name, email, age))

    connection.commit()
    cursor.close()

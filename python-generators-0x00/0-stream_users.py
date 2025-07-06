#!/usr/bin/env python3
import mysql.connector


def stream_users():
    """Generator that streams user rows one by one from the database."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # Replace with your MySQL user
            password="root",      # Replace with your MySQL password
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data;")

        for row in cursor:
            yield row

        cursor.close()
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if connection and connection.is_connected():
            connection.close()

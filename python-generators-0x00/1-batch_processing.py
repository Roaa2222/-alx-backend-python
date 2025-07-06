#!/usr/bin/env python3
import mysql.connector


def stream_users_in_batches(batch_size):
    """Generator to stream users in batches of `batch_size`."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # Use your credentials
            password="root",
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data;")

        while True:
            rows = cursor.fetchmany(batch_size)
            if not rows:
                break
            yield rows

        cursor.close()
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if connection and connection.is_connected():
            connection.close()


def batch_processing(batch_size):
    """Processes each batch and prints users with age > 25."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)

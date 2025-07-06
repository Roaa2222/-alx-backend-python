# 🐍 Python Generator – MySQL Seeder

This script:
- Connects to MySQL
- Creates a database `ALX_prodev`
- Creates a `user_data` table
- Loads data from `user_data.csv` using `insert_data()`

## Functions:
- `connect_db()`: connects to MySQL
- `create_database(connection)`: creates `ALX_prodev`
- `connect_to_prodev()`: connects to the new database
- `create_table(connection)`: creates `user_data` table
- `insert_data(connection, 'user_data.csv')`: seeds data if not exists

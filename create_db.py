import MySQLdb

try:
    # Try connecting without specifying a database first
    db = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="root"
    )
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS kissanbuddy_db")
    print("Database 'kissanbuddy_db' verified/created successfully.")
    db.close()
except MySQLdb.Error as e:
    print(f"Error: {e}")

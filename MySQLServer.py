import mysql.connector

def create_database():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Aliku_Mysql21!",
            database = "alx_book_store"
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        if cursor:  
            cursor.close()
        if connection: 
            connection.close()

if __name__ == "__main__":
    create_database()

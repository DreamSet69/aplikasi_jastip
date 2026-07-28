import mysql.connector
from mysql.connector import Error

def get_connection():
    hostname = "otla5b.h.filess.io"
    database = "pem_web_alsovowel"
    port = "61030"
    username = "pem_web_alsovowel"
    password = "5edd5a20244c7421b121771def4251d6271cf9ef"

    try:
        connection = mysql.connector.connect(
            host=hostname, 
            database=database, 
            user=username, 
            password=password, 
            port=port
        )
        if connection.is_connected():
            return connection
            
    except Error as e:
        print("Error while connecting to MariaDB", e)
        return None

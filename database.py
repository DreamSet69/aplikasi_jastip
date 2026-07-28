import pymysql

def get_connection():
    hostname = "otla5b.h.filess.io"
    database = "pem_web_alsovowel"
    port = 61030
    username = "pem_web_alsovowel"
    password = "5edd5a20244c7421b121771def4251d6271cf9ef"

    try:
        connection = pymysql.connect(
            host=hostname, 
            database=database, 
            user=username, 
            password=password, 
            port=port
        )
        return connection
    except Exception as e:
        print("Error while connecting to MariaDB", e)
        # We raise the exception so we can see the actual error on Vercel logs, 
        # or it can be handled by the app.
        raise e

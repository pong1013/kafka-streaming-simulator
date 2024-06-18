import pymysql
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def connect_to_mysql():
    return pymysql.connect(
        host='localhost',
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
    )
    
def exec_sql_file(file, connection):
    with open(file, 'r') as f:
        sql = f.read()
        
    with connection.cursor() as cursor:
        for statement in sql.split(';'):
            if statement.strip():
                cursor.execute(statement)
        connection.commit()
        
if __name__ == '__main__':
    conn = connect_to_mysql()
    print(conn.open)
    try:
        exec_sql_file('create_table.sql', conn)
        print("Table created successfully!")
    except Exception as e:
        print(f"Fail to create table: {e}")
    finally:
        conn.close
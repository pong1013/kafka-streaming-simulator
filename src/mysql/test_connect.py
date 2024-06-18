import pymysql
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

conn = pymysql.connect(
    host="127.0.0.1", user=os.getenv('MYSQL_USER'), password=os.getenv('MYSQL_PASSWORD'), database=os.getenv('MYSQL_DATABASE')
)
print(conn.open)
with conn.cursor() as cursor:
    print(cursor.execute("FLUSH PRIVILEGES"))
    print(
        cursor.execute(
            "SELECT user,host FROM mysql.user",
        )
    )
print(conn.ping())
conn.close()

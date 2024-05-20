import pymysql
import cryptography

# connect database 
db = pymysql.connect(
    host='localhost',
    user='root',
    password='@mysqlpassword202123',
)

# cursor to execute queries
cursor = db.cursor()



# Execute query to create the database 
query = "CREATE DATABASE IF NOT EXISTS Employee_DB"
cursor.execute(query)

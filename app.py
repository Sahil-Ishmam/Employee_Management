import pymysql
import cryptography


# connect Database 
db = pymysql.connect(
    host = "localhost",
    user = "root",
    password="@mysqlpassword202123",
    database="Employee_DB"
)

def create_table(table_name,cursor):
    query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
        Emp_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT,
        position VARCHAR(30) NOT NULL,
        salary INT DEFAULT 0,
        Performance INT DEFAULT 0
        );
        """
    cursor.execute(query)
    print(f"Table {table_name} created successfully")

def add_employee(table_name,name,age,position,salary,cursor):
    query = f"""

    INSERT INTO {table_name} 
    (name, age, position,salary)
    VALUES (%s, %s, %s, %s)

    """

    cursor.execute(query,(name,age,position,salary))  
    db.commit()






  



def Update_Performance(ID, name, performance, Table_Name, cursor):
    query = f"""
        UPDATE {Table_Name} SET performance = %s WHERE Emp_id = %s AND name = %s
    """
    cursor.execute(query, (performance, ID, name))
    db.commit()
    print("Performance updated successfully!")

def Update_Salary(ID,Name,Salary,Table_Name,cursor):
    query = f"""
        UPDATE {Table_Name} set Salary = %s Where Emp_id = %s AND name = %s     
    """

    cursor.execute(query,(Salary,ID,Name))
    db.commit()
    print("Salary has updated successfully !!!")

def Update_Position(ID,Name,Position,Table_Name,cursor):
    query = f"""
        UPDATE {Table_Name} set Position = %s Where Emp_id = %s AND name = %s
    """

    cursor.execute(query,(Position,ID,Name))
    db.commit()
    print("Position has Updated Successfully!!!!!!")


def View_Employees(Table_Name,cursor):
    query = f"""
        select * from {Table_Name};    
    """
    cursor.execute(query)
    
    all_info = cursor.fetchall()
    print("+------+----------------+-----+----------+--------+-------------+")
    print("| ID   | Name           | Age | Position | Salary | Performance |")
    print("+------+----------------+-----+----------+--------+-------------+")
    for emp in all_info:
        emp_id, name, age, position, salary, performance = emp
        print(f"| {emp_id:<4} | {name:<14} | {age:<3} | {position:<8} | {salary:<6} | {performance:<11} |")
        print("+------+----------------+-----+----------+--------+-------------+")

    """ 
    print("+--------+---------------+--------+-----------+---------+-------------+")
    print("| ID     | Name          | Age    | Position  | Salary  | Performance |")
    print("+--------+---------------+--------+-----------+---------+-------------+")
    
    for emp_info in all_info:
        emp_id,name,age,position,Salary,performance = emp_info
        print(f"| {emp_id}      | {name}          | {age}    | {position}    | {Salary}  | {performance} |")
     """
    print("All employee information is presented")

while(True):
    print(
        """
        1. create table 
        2. Add Employee
        3. Employee Performance Update
        4. Employee Salary Update
        5. Employee Position Update
        6. View Employee
        7. Exit 
        """
    )

    option = int(input("Choice an Option : "))

    if option==1:
        table_name = input("Enter Table Name : ")
        create_table(table_name,db.cursor())
    elif option==2:
        table_name = input("Enter table name : ")
        name = input("Enter Employee Name : ")
        age = int(input("Enter Age :"))
        position = input("Enter Position :")
        Salary = int(input("Enter salary : "))
        add_employee(table_name,name,age,position,Salary,cursor=db.cursor())
        print("employee inserted Successfully")  
    elif option==3:
        
        table_name = input("Enter table Name : ")
        ID = int(input("Enter Employee Id : "))
        Name = input("Enter Name : ")
        New_performance = int(input("Enter New Performance : "))

        Update_Performance(ID,Name,New_performance,Table_Name=table_name,cursor=db.cursor())


    elif option==4:

        table_name = input("Enter Table name : ")
        ID = int(input("Enter Employee ID : "))
        Name = input("Enter name :")
        New_salary = int(input("Enter New Salary : "))

        Update_Salary(ID,Name,New_salary,Table_Name=table_name,cursor=db.cursor())


    elif option ==5:

        table_name = input("Enter Table name : ")
        ID = int(input("Enter Employee ID : "))
        Name = input("Enter name :")
        New_position = input("Enter new Position : ")

        Update_Position(ID,Name,New_position,Table_Name=table_name,cursor=db.cursor())
        

    elif option == 6 :
        table_name = input("Enter Table name : ")

        View_Employees(Table_Name=table_name,cursor=db.cursor())

    elif option == 7:
        quit()
        


db.close()



  
        

        

            







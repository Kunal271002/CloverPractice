import pymysql
def Fetch():
    try:
        mydb = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="12345678",
            database="demodb"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM employee;")
        
        result = mycursor.fetchall()
        for row in result:
            print(row)

    except pymysql.MySQLError as err:
        print(f"Error: {err}")

    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()
def Add_Employee(emp_id,emp_name,salary,emp_role):
    try:
        mydb = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="12345678",
            database="demodb"
        )
        mycursor = mydb.cursor()
        query = "INSERT INTO employee(emp_id,emp_name,salary,emp_role) values (%s,%s,%s,%s)"
        mycursor.execute(query,(emp_id,emp_name,salary,emp_role))
        mydb.commit()
        print("Inserted")
    except pymysql.MySQLError as err:
        print(f"Error: {err}")

    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()
def FetechEmployee(emp_id):
    try:
        mydb = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="12345678",
            database="demodb"
        )
        mycursor = mydb.cursor()
        query = "SELECT * FROM employee where emp_id = %s;"
        print(query)
        mycursor.execute(query,{emp_id})
        
        result = mycursor.fetchall()
        for row in result:
            print(row)

    except pymysql.MySQLError as err:
        print(f"Error: {err}")

    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()
def Delete_Employee(emp_id):
    try:
        mydb = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="12345678",
            database="demodb"
        )
        mycursor = mydb.cursor()
        query = "Delete from employee where emp_id = %s"
        mycursor.execute(query,(emp_id))
        mydb.commit()
        print("Deleted")
    except pymysql.MySQLError as err:
        print(f"Error: {err}")

    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()
def Update_Employee(emp_id=0,emp_name="",salary=0,emp_role=""):
    try:
        mydb = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="12345678",
            database="demodb"
        )
        mycursor = mydb.cursor()
        if (not(emp_id == 0)) and (not (emp_name == ""))and (not (salary == 0)) and (not (emp_role == "")):
            query = "UPDATE employee SET emp_name=%s,salary=%s,emp_role=%s where emp_id = %s"
            mycursor.execute(query,(emp_name,salary,emp_role,emp_id))
            mydb.commit()
        print("Updates")
    except pymysql.MySQLError as err:
        print(f"Error: {err}")

    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()

# Fetch()
# Add_Employee(8,"Rishikesh",19375,"Trainee")
# FetechEmployee(4)
# Delete_Employee(4)
# Update_Employee(emp_id=8,emp_name="Rishi",salary=19375,emp_role="Trainee")
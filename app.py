from flask import Flask,redirect,render_template,request,url_for 
import pymysql
app = Flask(__name__)
def Get_Conn():
    mydb = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="12345678",
                database="demodb"
            )
    return mydb
    

@app.route("/")
def Index():
    return render_template("index.html")
    
@app.route("/Add",methods=['GET','POST'])
def Add():
    if request.method == "POST":
        Id = request.form["id"]
        Name = request.form["name"]
        Age =  request.form["age"]
        Salary = request.form["Salary"]
        mycursor = Get_Conn().cursor()
        query = "INSERT INTO employee(emp_id,emp_name,salary,emp_role) values (%s,%s,%s,%s)"
        mycursor.execute(query,(Id,Name,Salary,Age))
        Get_Conn().commit()
        mycursor.close()
        return "Employee Added Successfully"

@app.route("/Remove",methods=["POST"])
def Remove():
    if request.method == "POST":
        Id = request.form["id"]
        mycursor = Get_Conn().cursor()
        mycursor.execute(query,(Id))
        query = "Delete from employee where emp_id = %s"
        Get_Conn().commit()
        mycursor.close()
        return "Employee Deleted Successfully"

@app.route("/Update",methods=["POST"])
def Update():
    if request.method == "POST":
        Id = request.form["id"]
        Name = request.form["name"]
        Age =  request.form["age"]
        Salary = request.form["Salary"]
        mycursor = Get_Conn().cursor()
        query = "UPDATE employee SET emp_name=%s,salary=%s,emp_role=%s where emp_id = %s"
        mycursor.execute(query,(Name,Salary,Age,Id))
        Get_Conn().commit()
        mycursor.close()
        return "Employee Updated Successfully"

@app.route("/FetechAll")
def FetechAll():
    mycursor = Get_Conn().cursor()
    mycursor.execute("SELECT * FROM employee;")
    result = mycursor.fetchall()
    for row in result:
        print(row)
    Get_Conn().commit()
    mycursor.close()
    return render_template("FetchAllEmployee.html",result=result)

@app.route("/Fetch",methods=["POST"])
def Fetch():
    if request.method == "POST":
        Id = request.form["id"]
        mycursor = Get_Conn().cursor()
        query = "SELECT * FROM employee where emp_id = %s;"
        mycursor.execute(query,{Id})
        result = mycursor.fetchall()
        for row in result:
            print(row)
        Get_Conn().commit()
        mycursor.close()
        return render_template("FetchAllEmployee.html",result=result)

@app.route("/select",methods=["GET","POST"])
def Select():
    if request.method == "POST":
        EMployee = request.form["EmployeeMaster"]
        if EMployee == "Add":
            return render_template("AddEmployee.html")
        if EMployee == "Remove":
            return render_template("DeleteEmployee.html")
        if EMployee == "Update":
            return render_template("UpdateEmployee.html")
        if EMployee == "FetechAll":
            return redirect(url_for("FetechAll"))
        if EMployee == "Fetch":
            return render_template("Fetch.html")

if __name__=="__main__":
    app.run(debug=True)
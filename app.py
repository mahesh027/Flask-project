from flask import Flask,render_template,url_for,request,redirect
from flask_mysqldb import MySQL
app=Flask(__name__)
#Mysql connection
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="123456"

app.config["MYSQL_DB"]="crud"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)

#loading home page
@app.route("/")
def home():
  con= mysql.connection.cursor()
  sql="select * from users"
  con.execute(sql)
  res=con.fetchall()
  return render_template("home.html",datas=res) #render_template class 

#New User
@app.route("/addUsers",methods=['GET','POST'])
def addUsers():
    if request.method=='POST':
       name=request.form['name']
       city=request.form['city']
       age=request.form['age']
       con= mysql.connection.cursor()
       sql="insert into users (NAME,CITY,AGE) values(%s,%s,%s)"
       con.execute(sql,[name,city,age])
       mysql.connection.commit()
       con.close()
       return redirect(url_for("home"))
    return render_template("addUsers.html")
   
  
if(__name__== '__main__'):
    app.run(debug=True)
  
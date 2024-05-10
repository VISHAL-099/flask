from flask import Flask,render_template,redirect,url_for,request,session
import sqlite3
app = Flask(__name__)


#@app.route("/")
#def landingpage():
#  return render_template('base.html')

@app.route('/showdata')
def first():
  #connect database db1 and pull data from users table 
  con  = sqlite3.connect("db1")  # connect sms database
  con.row_factory = sqlite3.Row  # create object of Row
  cur = con.cursor()             # create cursor object, which will hold records 
                        # being fetched from database. 
  cur.execute( "select * from users ")  # execute a SQL query to get the data
  rows = cur.fetchall()          # all the data pulled from database is stored in rows object 
  con.close ()
  return render_template ('index.html' , data=rows)

@app.route('/')
def homepage():
  return render_template('home.html')


@app.route('/login')
def login():
  return render_template('login.html')






@app.route('/login1'  ,methods =["POST"] )
def login1():
  uemail = request.form.get("email")
  upwd   = request.form.get("pwd")
  
  # return str(uemail+upwd)
  # connect with database and check whether record 
  # exist with username having email as uemail and password as upwd.
  con  = sqlite3.connect("db1") 
  con.row_factory = sqlite3.Row
  cur = con.cursor() 
  cur.execute( "select * from users where email=='%s' and passwd=='%s'" %(uemail, upwd ))
  rows = cur.fetchall()
  con.close ()
#   uname =""
#   for r in rows :
#     uname  = r["username"]
    
#   if uname is ""  : 
#     return   redirect( url_for('login')) #str(" Invalid user ")
#   else :
#     session ["username"] = uname
#     return redirect( url_for('first'))
#     #return str("welcome :   " + session ["username"])
    
    
    
    
@app.route("/deluser")
def deleteuser():
   #connect database db1 and pull data from users table 
  con  = sqlite3.connect("db1")  # connect sms database
  con.row_factory = sqlite3.Row  # create object of Row
  cur = con.cursor()             # create cursor object, which will hold records 
                        # being fetched from database. 
  cur.execute( "select * from users ")  # execute a SQL query to get the data
  rows = cur.fetchall()          # all the data pulled from database is stored in rows object 
  con.close ()
  return render_template ('deluser.html' , data=rows)

@app.route('/delete' , methods = ["POST"])
def deleteuser1():
  uid = request.form.get("userid")
  #connect database db1 and pull data from users table 
  con  = sqlite3.connect("db1")  # connect sms database
  con.row_factory = sqlite3.Row  # create object of Row
  cur = con.cursor()             # create cursor object, which will hold records 
                        # being fetched from database. 
  cur.execute( "delete from users where userid="+ str(uid) )  # execute a SQL query to get the data
  con.commit()
  con.close ()
 
  return redirect(url_for('first'))


# #modify user data 
# @app.route('/modify')
# def updateuser():
#   uid = request.form.get("userid")
#   #connect database db1 and pull data from users table 
#   con  = sqlite3.connect("db1")  # connect sms database
#   con.row_factory = sqlite3.Row  # create object of Row
#   cur = con.cursor()             # create cursor object, which will hold records 
#                         # being fetched from database. 
#   cur.execute("select * from users where userid="+ str(uid))  # execute a SQL query to get the data
#   rows = cur.fetchall()
#   con.close ()
 
#   return  render_template ('modify.html',data=rows)

#modify user data 
@app.route('/modify' , methods = ["POST"])
def updateuser():
  uid = request.form.get("userid")
  #connect database db1 and pull data from users table 
  con  = sqlite3.connect("db1")  # connect sms database
  con.row_factory = sqlite3.Row  # create object of Row
  cur = con.cursor()             # create cursor object, which will hold records 
                        # being fetched from database. 
  cur.execute( "select * from users where userid="+ str(uid) )  # execute a SQL query to get the data
  rows = cur.fetchall()
  con.close ()
 
  return  render_template ('modify.html' , data=rows)

#modify user data 
@app.route('/modify1' , methods = ["POST"])
def updateuser1():
  uid = request.form.get("userid")
  username   = request.form.get("username")
  useremail  = request.form.get("useremail")
  userpasswd = request.form.get("userpasswd")
  
  #connect database db1 and pull data from users table 
  con  = sqlite3.connect("db1")  # connect sms database
  con.row_factory = sqlite3.Row  # create object of Row
  cur = con.cursor()             # create cursor object, which will hold records 
                        # being fetched from database. 
  cur.execute( "update users set username = '%s', email='%s', passwd='%s' where userid=%s" %(username,useremail,userpasswd,uid  ) ) 
  con.commit()
  con.close ()
 
  return  redirect(url_for('first'))




@app.route('/del/<uid>')
def deleterow(uid):
  #connect database db1 and pull data from users table 
  con  = sqlite3.connect("db1")  # connect sms database
  con.row_factory = sqlite3.Row  # create object of Row
  cur = con.cursor()             # create cursor object, which will hold records 
                        # being fetched from database. 
  cur.execute( "delete from users where userid="+ str(uid) )  # execute a SQL query to get the data
  con.commit()
  con.close ()
 
  return redirect(url_for('first'))





# add new record 
@app.route("/signup") 
def addnewrecord():
    return render_template("addform.html")

 

  
  
  
  
@app.route("/add" ,methods =["POST"])
def addnewrecord1():
  userid     = request.form.get("userid")
  username   = request.form.get("username")
  useremail  = request.form ["useremail"]
  userpasswd = request.form.get("userpasswd")
  
  con  = sqlite3.connect("db1")  
  con.row_factory = sqlite3.Row  
  cur = con.cursor()              
  cur.execute("INSERT INTO users (userid, username,gmail, password) \
              VALUES (%s,'%s','%s','%s')"%(userid,username,useremail,userpasswd))
  #cur.execute("INSERT INTO users (userid, username, email, passwd) VALUES (11 , 'amit','amit@gmail.com','aa')")          
  
  con.commit()
  con.close ()
  
  return redirect(url_for('first'))
  
  

# define another route 
@app.route('/s')
def second():
  return '<html> this is new route <h1> AIML </h1></html> '

if __name__ == '__main__':
  app.run()
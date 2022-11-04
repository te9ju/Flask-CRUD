from flask import Flask,render_template, request, redirect, url_for
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proj_db'
 
mysql = MySQL(app)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/editForm')
def editForm():
    args = request.args
    id = args.get("id")
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM users WHERE userId = %s''',(id))
    data = cursor.fetchall()
    return render_template('editForm.html', data=data)
 
@app.route('/editUser', methods = ['POST', 'GET'])
def editUser():
    id = request.form['id']
    userName = request.form['userName']
    password = request.form['password']
    cursor = mysql.connection.cursor()
    cursor.execute(''' UPDATE users SET userName = %s, password = %s WHERE userId = %s''',(userName,password, id))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('list'))

@app.route('/signup', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Sign up via the sign up form"
     
    if request.method == 'POST':
        userName = request.form['userName']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO users(userName, password) VALUES(%s,%s)''',(userName,password))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"

@app.route('/delete')
def delete():
    args = request.args
    id = args.get("id")
    cursor = mysql.connection.cursor()
    cursor.execute(''' DELETE FROM users WHERE userId = %s''',(id))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('list'))

@app.route('/list')
def list():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM users''')
    data = cursor.fetchall()
    return render_template('list.html', data=data)
    
app.run(host='localhost', port=5000)
if __name__ == '__main__':
    app.debug = True
    app.run()   
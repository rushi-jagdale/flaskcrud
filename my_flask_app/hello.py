from flask import Flask,flash, render_template, request,url_for,redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'mis_user'
app.config['MYSQL_PASSWORD'] = 'india#123'
app.config['MYSQL_DB'] = 'myadmin'

# Intialize MySQL
mysql = MySQL(app)


@app.route('/new', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        Fullname = request.form['Fullname']
        Email = request.form['Email']
        Password = request.form['Password']
        cur = mysql.connection.cursor()
        cur.execute(" INSERT INTO users VALUES(0,%s,%s,%s)",(Fullname,Email,Password))
        mysql.connection.commit()
        cur.close()
    return render_template('add.html')


@app.route('/')
def example():
    cur = mysql.connection.cursor()
    cur.execute(" SELECT * FROM users")
    output = cur.fetchall()
    return render_template('example.html', output = output)


@app.route('/edit/<int:id_data>')
def edit(id_data):
    cur = mysql.connection.cursor()
    cur.execute(" SELECT * FROM users WHERE id=%s",(id_data,))
    output = cur.fetchone()
    cur.close()
    return render_template('edit.html', output = output)


@app.route('/up', methods=['POST'])
def update():
    id_data = request.form['id']
    Fullname = request.form['Fullname'] 
    Email = request.form['Email']
    Password = request.form['password']   
    cur = mysql.connection.cursor()
    cur.execute(" UPDATE users SET Fullname=%s, Email=%s, Password=%s WHERE id=%s",(Fullname,Email,Password,id_data,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('example'))


@app.route('/delete/<int:id_data>', methods=['GET'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute(" DELETE FROM users WHERE id=%s",(id_data,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('example'))


 

if __name__ == '__main__':
    app.run(debug=True)    


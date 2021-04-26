from flask import * 
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "abc" 

# Enter your database connection details below
app.config['MYSQL_USER'] = 'mis_user'
app.config['MYSQL_DB'] = 'myadmin'
app.config['MYSQL_PASSWORD'] = 'india#123'
app.config['MYSQL_HOST'] = 'localhost'
# Intialize MySQL

mysql = MySQL(app)


@app.route('/')
def example():
    cur = mysql.connection.cursor()
    cur.execute(" SELECT * FROM users")
    output = cur.fetchall()
    flash("you are successfuly logged in")  
    return render_template('index.html', output = output)


if __name__ == '__main__':
    app.run()

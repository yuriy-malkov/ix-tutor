from flask import Flask, request, Response
from flask_mysqldb import MySQL

APP = Flask(__name__)
APP.config['MYSQL_HOST'] = 'localhost'
APP.config['MYSQL_USER'] = 'root'
APP.config['MYSQL_PASSWORD'] = 'root'
APP.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(APP)

class User:
    def __init__(self, email, password):
        self.userID = None
        self.email = email
        self.password = password
        self.isTutor = False
        self.isStudent = False

    def insert_into_db(self):
        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Users(email, password) VALUES (%s, %s)", (self.email, self.password))
            mysql.connection.commit()
            cur.close()
            return Response(status=200)
        except e:
            print(e)
            return Response(status=504)



@APP.route('/user/register', methods=['POST'])
def create_user():
    email = request.form['email']
    password = request.form['password']
    new_user = User(email, password)
    new_user.insert_into_db():

@APP.route('/user/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']


def get_user(email, password):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Users WHERE email = %s and password = %s", (email, password))
    data = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return userID


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=80)
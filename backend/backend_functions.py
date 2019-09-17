from flask import Flask, request, jsonify

APP = Flask(__name__)

count = 4
test_users = [
    {
        'userID' : 1,
        'email' : "first@gmail.com",
        'password' : "password",
        'isTutor' : False,
        'isStudent' : False
    },
    {
        'userID' : 2,
        'email' : "second@gmail.com",
        'password' : "password",
        'isTutor' : True,
        'isStudent' : False
    },
    {
        'userID' : 3,
        'email' : "third@gmail.com",
        'password': "password",
        'isTutor' : True,
        'isStudent' : True
    }
]

class User:
    def __init__(self, email, password):
        self.userID = None
        self.email = email
        self.password = password
        self.isTutor = False
        self.isStudent = False

    '''
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
    '''



@APP.route('/user/register', methods=['POST'])
def create_user():
    print(request.data)
    email = request.json['email']
    password = request.json['password']
    global count


    # new_user = User(email, password)
    
    #new_user.insert_into_db():
    
    # test_users.append({
    #     'userID' : 4,
    #     'email' : new_user.email,
    #     'password' : new_user.password,
    #     'isTutor' : False,
    #     'isStudent' : False
    # })

    test_users.append({
        'userID' : count,
        'email' : email,
        'password' : password,
        'isTutor' : False,
        'isStudent' : False
    })

    count += 1
    return jsonify(test_users)
    

@APP.route('/user/login', methods=['GET'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = get_user(email, password)    
    print(user)

@APP.route('/user/getUser', methods=['GET'])
def get_user(email, password):
    email = request.json['email']
    password = request.json['password']
    for user in test_users:
        if user[email] == email and user[password] == password:
                 return jsonify(user)



if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=80)

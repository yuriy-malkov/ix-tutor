from flask import Flask, request, jsonify
import psycopg2

APP = Flask(__name__)
APP.config['DEBUG'] = True

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

def get_user_from_login(email, password):
    # Need to query DB for user based on email and pass
    for user in test_users:
        if user[email] == email and user[password] == password:
                 return user

def get_user_from_id(userID):
    # Need to query DB for user based on ID
    for user in test_users:
        if user[userID] == userID:
            return user


@APP.route('/user/register', methods=['POST'])
def create_user():
    print(request.data)
    email = request.json['email']
    password = request.json['password']
    global count

    # new_user = User(email, password)
    #new_user.insert_into_db()

    test_users.append({
        'userID' : count,
        'email' : email,
        'password' : password,
        'isTutor' : False,
        'isStudent' : False,
        'enrollments' : []
    })

    count += 1
    return jsonify(test_users[-1])
    

@APP.route('/user/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = get_user_from_login(email, password)    
    return jsonify(user)

@APP.route('/user/setType', methods=['POST'])
def set_user_type():
    userID = request.form['userID']
    user = get_user_from_id(userID)

    isTutor = request.form['isTutor']
    if isTutor:
        user.isTutor = True
        #With DB need to set user attribute within DB
    else:
        user.isStudent = True
        #With DB need to set user attribute within DB

@APP.route('/student/viewAllBookings', methods = ['GET'])
def view_all_bookings():

    '''
    - Will query db for all created bookings, something like:
    - SELECT * FROM TutorBooking
    '''

@APP.route('/student/searchBookings', methods = ['POST'])
def search_bookings():
    
    '''
    - Filter all available bookings via parameters
        - Date range
        - Location
        - Interest
    - SELECT * FROM TutorBooking WHERE ...
    '''

@APP.route('/student/enrollments', methods=['POST'])
def get_student_enrollments():
    userID = request.form['userID']
    user = get_user_from_id(userID)

    '''
    Will need to change to db query:
    SELECT bookingID FROM Student_Enroll WHERE userID = %s (userID)

    or something similar
    '''

    return jsonify(user)

@APP.route('/student/addEnrollment', methods=['POST'])
def student_add_enrollment():
    userID = request.form['userID']
    # How to send booking?
    bookingID = request.form['bookingID']
    user = get_user_from_id(userID)

    '''
    Will need to change to db query to ADD to Student_Enroll or something

    Need to update the booking to show that student is enrolled from tutor view
    '''

@APP.route('/student/removeEnrollment', methods=['POST'])
def student_remove_enrollment():
    userID = request.form['userID']
    bookingID = request.form['bookingID']
    user = get_user_from_id(userID)

    '''
    Will need to change to db query to DELETE from Student_Enroll or something

    Need to update the booking to show that student is no longer enrolled from tutor view
    '''
    user.enrollments.remove(bookingID)

@APP.route('/tutor/showBookings', methods=['POST'])
def tutor_show_bookings():
    userID = request.form('userID')
    user = get_user_from_id(userID)


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=80)  

'''
###############
TUTOR ROUTES###
###############

###IN PROGRESS###

Tutor - show bookings
Tutor - add booking
Tutor - edit booking
Tutor - delete booking
Tutor - delete booking on timeout (no one enrolled within 24hours of booking start time, delete)
Tutor - show all available requests
Tutor - search available requests (via date range, location, interest)
'''

'''
#################
STUDENT ROUTES###
#################

###DONE###



###BLOCKED###

Student - show enrollments 
Student - show all available bookings
Student - search available bookings (via date range, location, interest)
Student - add enrollment
    - update booking with enrollment (should show on tutor booking)
Student - delete enrollment
    - update booking with removal of enrollment (should show on tutor booking)

###IN PROGRESS###

Student - request booking
'''

'''
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
'''
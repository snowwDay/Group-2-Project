"""
Main module: Driver for software functionality

Accepts requests from time clock app
Stores user information for later management
Returns information stored from users
"""
from flask import Flask, request, redirect, jsonify, make_response
from flask_talisman import Talisman
from flask_seasurf import SeaSurf
from Db import *
from Utils import *
from Hasher import *

Debug=True
Host='137.184.96.25'
Port=2000

app = Flask(__name__)
Talisman(app)
csrf = SeaSurf(app)

key = 'TempKey'


"""
Auth function: Checks to see if a user has been authorized

:param token: Token supplied by user
:return: Either None, or a tuple containing user id and auth level
"""
def auth(token):
    if token is None:
        return None
    sched_cursor.execute(f'select sID,ranks from tokens where token=to_base64(aes_encrypt(%s,"{key}")) ORDER BY creationDate DESC LIMIT 1;', (token,))
    creds = sched_cursor.fetchone()
    if creds is not None:
        return creds
    return None

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

"""
login_staff function: Used to log normal staff members in

:path: /login

:param user: Username attempting to login
:param pass: Password of user attempting to login
:return: Auth token on successful login
"""
@app.route('/login_staff', methods=['GET'])
def login_staff():
    if 'user' in request.args and 'pass' in request.args:
        sPass = request.args.get('pass')
        user = request.args.get('user')
        if sPass is None or user is None:
            return make_response(jsonify( { 'Error:': 'Not all information supplied.'}), 501)
        emp_cursor.execute(f'select sID from staff where sUsername=to_base64(aes_encrypt(%s,"{key}"));', (user,))
        temp_sID = emp_cursor.fetchone()[0]
        sched_cursor.execute(f'select convert(aes_decrypt(from_base64(salt),"{key}"),CHAR) from staff_salts where sID=%s;', (temp_sID,))
        salt = sched_cursor.fetchone()[0]
        emp_cursor.execute(f'select to_base64(aes_encrypt(%s,"{key}"))', (sPass,))
        sPass = emp_cursor.fetchone()[0]
        sPass = Hasher.generate_hash(sPass, salt)
        emp_cursor.execute(f'select sID from staff where sUserName=to_base64(aes_encrypt(%s,"{key}")) and sPassword=%s', (user,sPass))
        sID = emp_cursor.fetchone()
        if sID is not None:
            token = utils.gen_token(32)
            sched_cursor.execute(f'insert into tokens(sID,token,ranks)values(%s,to_base64(aes_encrypt(%s,"{key}")),1);', (sID[0], token))
            sched_db.commit()
            return make_response(jsonify( { 'Token': token } ), 200)
    return make_response(jsonify( { 'Error:': 'Invalid Credentials' } ), 401)

"""
login_admin function: Used to log admin members in

:path: /login_admin 72aSLupVe90kOdApfqn7rg==

:param user: Username attempting to login
:param pass: Password of user attempting to login
:return: Auth token on successful login
"""
@app.route('/login_admin', methods=['GET'])
def login_admin():
    if 'user' in request.args and 'pass' in request.args:
        sPass = request.args.get('pass')
        #hash user and pass
        user = request.args.get('user')
        if sPass is None or user is None:
            return make_response(jsonify( { 'Error:': 'Not all information supplied.'}), 501)
        emp_cursor.execute(f'select aID from admin where aUsername=to_base64(aes_encrypt(%s,"{key}"));', (user,))
        temp_sID = emp_cursor.fetchone()[0]
        sched_cursor.execute(f'select convert(aes_decrypt(from_base64(salt),"{key}"),CHAR) from admin_salts where aID=%s;', (temp_sID,))
        salt = sched_cursor.fetchone()[0]
        emp_cursor.execute(f'select to_base64(aes_encrypt(%s,"{key}"))', (sPass,))
        sPass = emp_cursor.fetchone()[0]
        sPass = Hasher.generate_hash(sPass, salt)
        emp_cursor.execute(f'select aID from admin where aUserName=to_base64(aes_encrypt(%s,"{key}")) and aPass=%s', (user,sPass))
        sID = emp_cursor.fetchone()
        if sID is not None:
            token = utils.gen_token(32)
            sched_cursor.execute(f'insert into tokens(sID,token,ranks)values(%s,to_base64(aes_encrypt(%s,"{key}")),2);', (sID[0], token))
            sched_db.commit()
            return make_response(jsonify( { 'Token': token } ), 200)
        else:
            return make_response(jsonify( { 'Error:': 'sadasdadadadad' } ), 401)
    return make_response(jsonify( { 'Error:': 'Invalid Credentials' } ), 401)

"""
add_staff function: Used to add new staff members to the system

:path: /add_staff

:param dID: Department that the user will belong to
:param name: Name of user to be added
:param user: Username of user to be added
:param pass: Password of user to be added
:return: Message on success or failure
"""
@app.route('/add_staff', methods=['POST'])
def add_staff():
    creds = auth(request.args.get('token'))
    if creds is not None and creds[1] == 2:
        sEmail = request.args.get('email')
        sName = request.args.get('name')
        sUsername = request.args.get('user')
        sPass = request.args.get('pass')
        #salt = utils.gen_token(15)
        #sPass = generate_hash(sPass, salt)
        emp_cursor.execute(f'select count(1) from staff where sUsername=to_base64(aes_encrypt(%s,"{key}"))',(sUsername,))
        if emp_cursor.fetchone()[0] > 0:
            return make_response(jsonify( { 'Error:': 'User already exists.' } ), 502)
        emp_cursor.execute(f'select to_base64(aes_encrypt(%s,"{key}"))', (sPass,))
        sPass = emp_cursor.fetchone()[0]
        salt = utils.gen_token(32)
        sPass = Hasher.generate_hash(sPass, salt)
        emp_cursor.execute(f'insert into staff (sEmail, sName, sUsername, sPassword)values(to_base64(aes_encrypt(%s,"{key}")), to_base64(aes_encrypt(%s,"{key}")), to_base64(aes_encrypt(%s,"{key}")), %s)',(sEmail, sName, sUsername, sPass))
        emp_db.commit()
        sched_cursor.execute(f'insert into staff (admin, sName)values(%s,to_base64(aes_encrypt(%s,"{key}")))',(creds[0], sName))
        sched_db.commit()
        emp_cursor.execute(f'select sID from staff where sUsername=to_base64(aes_encrypt(%s,"{key}")) and sPassword=%s;', (sUsername, sPass))
        sID = emp_cursor.fetchone()[0]
        sched_cursor.execute(f'insert into staff_salts (sID,salt)values(%s,to_base64(aes_encrypt(%s,"{key}")));', (sID,salt))
        sched_db.commit()
        return make_response(jsonify( { 'Message': f'User {sUsername} has been created' } ), 200)
    else:
        return make_response(jsonify( { 'Error:': 'Unauthorized Access...' } ), 501)

"""
add_admin function: Used to add new admin members to the system

:path: /add_admin

:param dID: Department that the user will belong to
:param name: Name of user to be added
:param user: Username of user to be added
:param pass: Password of user to be added
:return: Message on success or failure
"""
@app.route('/add_admin', methods=['POST'])
def add_admin():
    #creds = auth(request.args.get('token'))
    if True or creds is not None and creds[1] == 3:
        sEmail = request.args.get('email')
        sName = request.args.get('name')
        sUsername = request.args.get('user')
        sPass = request.args.get('pass')
        emp_cursor.execute(f'select count(1) from admin where aUsername=to_base64(aes_encrypt(%s,"{key}"))',(sUsername,))
        if emp_cursor.fetchone()[0] > 0:
            return make_response(jsonify( { 'Error:': 'User already exists.' } ), 502)
        emp_cursor.execute(f'select to_base64(aes_encrypt(%s,"{key}"))', (sPass,))
        sPass = emp_cursor.fetchone()[0]
        salt = utils.gen_token(32)
        sPass = Hasher.generate_hash(sPass, salt)
        emp_cursor.execute(f'insert into admin (aName, aEmail, aUsername, aPass)values(to_base64(aes_encrypt(%s,"{key}")), to_base64(aes_encrypt(%s,"{key}")), to_base64(aes_encrypt(%s,"{key}")), %s)',(sName, sEmail, sUsername, sPass))
        emp_db.commit()
        sched_cursor.execute(f'insert into admin (aName)values(to_base64(aes_encrypt(%s,"{key}")))',(sName,))
        sched_db.commit()
        emp_cursor.execute(f'select aID from admin where aUsername=to_base64(aes_encrypt(%s,"{key}")) and aPass=%s;', (sUsername, sPass))
        sID = emp_cursor.fetchone()[0]
        sched_cursor.execute(f'insert into admin_salts (aID,salt)values(%s,to_base64(aes_encrypt(%s,"{key}")));', (sID,salt))
        sched_db.commit()
        return make_response(jsonify( { 'Message': f'User {sUsername} has been created' } ), 200)
    else:
        return make_response(jsonify( { 'Error:': 'Unauthorized Access...' } ), 501)

"""
remove_staff function: Used to add remove staff members from the system

:path: /remove_staff

:param sID: Id of staff member to be removed
:return: Message on success or failure
"""
@app.route('/remove_staff', methods=['POST'])
def remove_staff():
    creds = auth(request.args.get('token'))
    if creds is not None and creds[1] == 2:
        sID = request.args.get('sID')
        emp_cursor.execute(f'delete from staff where admin=%s and sID=%s LIMIT 1',(creds[0],sID))
        emp_db.commit()
        sched_cursor.execute(f'delete from staff where admin=%s and sID=%s LIMIT 1',(creds[0],sID))
        sched_db.commit()
        return make_response(jsonify( { 'Message': f'User {sID} has been removed from staff' } ), 200)
    else:
        return make_response(jsonify( { 'Error:': 'Invalid Credentials' } ), 401)

"""
remove_admin function: Used to add remove admin members from the system

:path: /remove_admin

:param sID: Id of admin member to be removed
:return: Message on success or failure
"""
@app.route('/remove_admin', methods=['POST'])
def remove_admin():
    creds = auth(request.args.get('token'))
    if creds is not None and cerds[1] == 2:
        emp_cursor.execute(f'delete from admin where aID=%s LIMIT 1',(creds[0],))
        emp_db.commit()
        sched_cursor.execute(f'delete from admin where aID=%s LIMIT 1',(creds[0],))
        sched_db.commit()
        return make_response(jsonify( { 'Message': f'User {sID} has been removed from admin' } ), 200)
    else:
        return make_response(jsonify( { 'Error:': 'Invalid Credentials' } ), 401)

"""
get_user function: Used to get all info on a user

:path: /get_user

:param token: Authenticate user
:param sID: If admin, can get information of their staff member
:return: User information
:return: Success or Failure
"""
@app.route('/get_user', methods=['GET'])
def get_user():
    creds = auth(request.args.get('token'))
    if creds is not None:
        try:
            if creds[1] == 1:
                sched_cursor.execute(f'select sID,dID,convert(aes_decrypt(from_base64(sName),"{key}"),CHAR) from staff where sID=%s;', (creds[0],))
                user = sched_cursor.fetchone()
                sched_cursor.execute(f'select id,sID,UNIX_TIMESTAMP(startTime),UNIX_TIMESTAMP(endTime),timeOff from schedule where sID=%s;', (creds[0],))
                sched = sched_cursor.fetchall()
            elif creds[1] == 2:
                sID = request.args.get('sID')
                if sID is not None:
                    sched_cursor.execute(f'select sID,dID,convert(aes_decrypt(from_base64(sName),"{key}"),CHAR) from staff where sID=%s;', (sID,))
                    user = sched_cursor.fetchone()
                    sched_cursor.execute(f'select id,sID,UNIX_TIMESTAMP(startTime),UNIX_TIMESTAMP(endTime),timeOff from schedule where sID=%s;', (sID,))
                    sched = sched_cursor.fetchall()
                else:
                    sched_cursor.execute(f'select aID,dID,convert(aes_decrypt(from_base64(aName),"{key}"),CHAR) from admin where aID=%s;', (creds[0],))
                    user = sched_cursor.fetchone()
                    sched = None

            if user is not None:
                return make_response(jsonify( { 'UserData': str(user), 'Schedule': str(sched) } ), 200)
            else:
                return make_response(jsonify( { 'Error': 'User not found!' } ), 404)
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)
    return make_response(jsonify( { 'Error': 'User not authorized!' } ), 501)

"""
update_user function: Update user's information

:path: /update_user

:param token: Authenticate user
:param dID: New department ID to apply
:param email: New email address
:param name: Change name on account
:return: Success or Failure
"""
@app.route('/update_user', methods=['POST'])
def update_user():
    creds = auth(request.args.get('token'))
    if creds is not None:
        try:
            dID = request.args.get('dID')
            email = request.args.get('email')
            name = request.args.get('name')

            if creads[0] == 1:
                table = staff
                prefix = 's'
            else:
                table = admin
                prefix = 'a'

            if dID is not None:
                emp_cursor.execute(f'UPDATE %s set dID=%s where %sID=%s LIMIT 1', (table,dID,prefix,creds[0]))
                emp_db.commit()
                sched_cursor.execute(f'UPDATE %s set dID=%s where %sID=%s LIMIT 1', (table,dID,prefix,creds[0]))
                sched_db.commit()
            if email is not None:
                emp_cursor.execute(f'UPDATE %s set %sEmail=to_base64(aes_encrypt(%s,"{key}")) where %sID=%s LIMIT 1', (table,prefix,email,creds[0]))
                emp_db.commit()
            if name is not None:
                emp_cursor.execute(f'UPDATE %s set %sName=to_base64(aes_encrypt(%s,"{key}")) where %sID=%s LIMIT 1', (table,prefix,name,creds[0]))
                emp_db.commit()
                sched_cursor.execute(f'UPDATE %s set %sName=to_base64(aes_encrypt(%s,"{key}")) where %sID=%s LIMIT 1', (table,prefix,name,creds[0]))
                sched_db.commit()

        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)
            return make_response(jsonify( { 'Error': 'Internal system error.' }), 503)
    else:
        return make_response(jsonify( { 'Response': 'Error. User not permittedd to do this.' }), 501)

"""
reset_pass function: Used to change/reset password

:path: /reset_pass

:param token: Authenticate user
:param pass: New password to apply
:return: Success or Failure
"""
@app.route('/reset_pass', methods=['POST'])
def reset_pass():
    sID = auth(request.args.get('token'))
    new_pass = request.args.get('pass')
    if sID is not None and new_pass is not none:
        try:
           #create hash and salt and store as  new_pass
           emp_cursor.execute(f'UPDATE staff set sPassword=to_base64(aes_encrypt(%s,"{key}")) where sID=%s', (new_pass, sID))
           emp_db.commit()
           return make_response(jsonify( { 'Response': 'Password has been reset.' }), 200)

        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)
            return make_response(jsonify( { 'Error': 'Internal system error.' }), 503)
    else:
        return make_response(jsonify( { 'Response': 'Error. User is not authorized to do this.' }), 501)

"""
add_schedule function: Used to add a scheduled date

:path: /add_schedule

:param token: Authenticate user
:param sID: sID of staff member to add to
:param start: Start time/date
:param end: Ending time/date
:param timeOff: Is this an addition of ttime off
:return: Success or Failure
"""
@app.route('/add_schedule', methods=['POST'])
def add_schedule():
    creds = auth(request.args.get('token'))
    if creds is not None and creds[1] == 2:
        try:
            sID = request.args.get('sID')
            start_time = request.args.get('start')
            end_time = request.args.get('end')
            time_off = request.args.get('timeOff')
            sched_cursor.execute(f'insert into schedule (sID,workDate,startTime,endTime,timeOff)values(%s,FROM_UNIXTIME(%s/1000),FROM_UNIXTIME(%s/1000),FROM_UNIXTIME(%s/1000),%s);', (sID, start_time, start_time, end_time, time_off))
            sched_db.commit()
            return make_response(jsonify( { 'Response': 'Schedule updated.' }), 200)
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)
            return make_response(jsonify( { 'Error': 'Internal system error.' }), 503)
    return make_response(jsonify( { 'Error': 'Unauthorized access.' }), 501)

"""
remove_schedule function: Used to remove a scheduled date

:path: /remove_schedule

:param token: Authenticate user
:param id: id of schedule item to remove
:return: Success or Failure
"""
@app.route('/remove_schedule', methods=['POST'])
def remove_schedule():
    creds = auth(request.args.get('token'))
    if creds is not None and creds[1] == 2:
        try:
            id = request.args.get('id')
            sched_cursor.execute(f'delete from schedule where id=%s;', (id,))
            sched_db.commit()
            return make_response(jsonify( { 'Response': 'Schedule updated.' }), 200)
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)
            return make_response(jsonify( { 'Error': 'Internal system error.' }), 503)

"""
add_department function: Used to add a department under admin

:path: /add_department

:param token: Authenticate user
:param dep: Name of department to add
:return: Success or Failure
"""
@app.route('/add_department', methods=['POST'])
def add_department():
    creds = auth(request.args.get('token'))
    if creds is not None and creds[1] == 2:
        try:
            dep = request.args.get('dep')
            sched_cursor.execute(f'select dID from department where dName=to_base64(aes_encrypt(%s,"{key}"))', (dep, ))
            if cursor.fetchone() is None:
                emp_cursor.execute(f'insert into department (dName,aID)values(to_base64(aes_encrypt(%s,"{key}")),%s)', (dep, creds[0]))
                emp_db.commit()
                sched_cursor.execute(f'insert into department (dName,aID)values(to_base64(aes_encrypt(%s,"{key}")),%s)', (dep, creds[0]))
                sched_db.commit()
                return make_response(jsonify( { 'Response': 'Department has been added.' } ), 200)
            else:
                return make_response(jsonify( { 'Response': 'Department already exists' } ), 400)
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)
            return make_response(jsonify( { 'Error': 'Internal system error.' }), 503)

"""
remove_department function: Used to remove a department under admin

:path: /remove_department

:param token: Authenticate user
:param id: ID of department to remove
:return: Success or Failure
"""
@app.route('/remove_department', methods=['POST'])
def remove_department():
    creds = auth(request.args.get('token'))
    if creds is not None and creds[1] == 2:
        try:
            dID = request.args.get('dID')
            sched_cursor.execute(f'select dID from department where dID=%s and aID=%s', (dID, creds[0]))
            if cursor.fetchone() is not None:
                emp_cursor.execute(f'delete from department where dID=%s and aID=%s', (dep, creds[0]))
                emp_db.commit()
                sched_cursor.execute(f'delete from department where dID=%s and aID=%s', (dep, creds[0]))
                sched_db.commit()
                return make_response(jsonify( { 'Response': 'Department has been removed.' } ), 200)
            else:
                return make_response(jsonify( { 'Response': 'Department does not exist' } ), 501)
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)
            return make_response(jsonify( { 'Error': 'Internal system error.' }), 503)

"""
get_departments function: Used to retrieve all departments owned by admin

:path: /get_departments

:param token: Authenticate user
:return: List of departments
:return: Success or Failure
"""
@app.route('/get_departments', methods=['GET'])
def get_departments():
    creds = auth(request.args.get('token'))
    if creds is not None and creds[1] == 2:
        try:
            sched_cursor.execute(f'select dID,convert(aes_decrypt(from_base64(dName),"{key}"), CHAR) from department where aID=%s', (creds[0], ))
            deps = sched_cursor.fetchall()
            if deps is not None:
                return make_response(jsonify( { 'Departments': deps } ), 200)
            else:
                return make_response(jsonify( { 'Error': 'You do not have any departments...' } ), 404)
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)
            return make_response(jsonify( { 'Error': 'Internal system error.' }), 503)

"""
get_staff function: Used to retrieve all departments owned by admin

:path: /get_staff

:param token: Authenticate user
:return: List of staff members
:return: Success or Failure
"""
@app.route('/get_staff', methods=['GET'])
def get_staff():
    creds = auth(request.args.get('token'))
    if creds is not None and creds[1] == 2:
        try:
            sched_cursor.execute(f'select sID,dID,convert(aes_decrypt(from_base64(sName),"{key}"), CHAR) from staff where admin=%s', (creds[0], ))
            staff = sched_cursor.fetchall()
            if staff is not None:
                return make_response(jsonify( { 'Response': staff } ), 200)
            else:
                return make_response(jsonify( { 'Response': 'You do not have any staff.' } ), 400)
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)
            return make_response(jsonify( { 'Error': 'Internal system error.' }), 503)

"""
clock_in function: Clock in for staff members

:path: /clock_in

:param token: Authenticate user
:return: Success or Failure
"""
@app.route('/clock_in', methods=['POST'])
def clock_in():
    creds = auth(request.args.get('token'))
    if creds is not None and creds[1] == 1:
        try:
            sched_cursor.execute(f'insert into clock (sID,clockIn,status)values(%s,now(),"In")', (creds[0],))
            sched_db.commit()
            return make_response(jsonify( { 'Response': 'Clocked In' } ), 200)
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)
            return make_response(jsonify( { 'Error': 'Internal system error.' }), 503)
    return make_response(jsonify( { 'Error': 'Unauthorized access!' } ), 501)

"""
clock_out function: Clock out for staff members

:path: /clock_out

:param token: Authenticate user
:return: Success or Failure
"""
@app.route('/clock_out', methods=['POST'])
def clock_out():
    creds = auth(request.args.get('token'))
    if creds is not None and creds[1] == 1:
        try:
            status = request.args.get('status')
            if status is None:
                return make_response(jsonify( { 'Error:': 'Not all information supplied.'}), 501)
            sched_cursor.execute(f'insert into clock (sID,clockOut,status)values(%s,now(),%s)', (creds[0],status))
            sched_db.commit()
            return make_response(jsonify( { 'Response': 'Clocked out.' } ), 200)
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)
            return make_response(jsonify( { 'Error': 'Internal system error.' }), 503)

"""
get_status function: Get clock status of staff member

:path: /get_status

:param token: Authenticate user
:param sID: ID of staff member, used as admin
:return: Success or Failure
"""
@app.route('/get_status', methods=['GET'])
def get_status():
    creds = auth(request.args.get('token'))
    sID = request.args.get('sID')
    if creds is not None:
        try:
            if creds[1] == 1:
                sched_cursor.execute(f'select status from clock where sID=%s ORDER BY id DESC LIMIT 1', (creds[0],))
            else:
                if sID is None:
                    return make_response(jsonify( { 'Error': 'Please supply staff member' } ), 502)
                sched_cursor.execute(f'select status from clock where sID=%s and admin=%s ORDER BY id DESC LIMIT 1', (sID,creds[0]))
            status = sched_cursor.fetchone()
            if status is None:
                return make_response(jsonify( { 'Response': 'User has never clocked in.' } ), 404)
            return make_response(jsonify( { 'Status': status[0] } ), 200)
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)
            return make_response(jsonify( { 'Error': 'Internal system error.' }), 503)

if __name__ == "__main__":
    import logging
    logging.basicConfig(filename='_api.log',level=logging.DEBUG)
    app.secret_key = 'super secret key'
    app.run(debug=Debug, host=Host, port=Port)
    app.run(ssl_context=('cert.pem', 'key.pem'), host=Host, port=Port, debug=Debug)

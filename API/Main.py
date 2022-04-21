from flask import Flask, request, redirect, jsonify, make_response
from Db import *
from Utils import *
from Hasher import *

Debug=True
Host='137.184.96.25'
Port=3000

app = Flask(__name__)

def auth(arg):
    if arg is None:
        return -1
    cursor.execute('select sID,rank from tokens where token=%s ORDER BY creationDate DESC LIMIT 1;', (arg,))
    creds = cursor.fetchone()[0]
    if creds is not None:
        return creds
    return None

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/login', methods=['GET'])
def login_staff():
    if 'user' in request.args and 'pass' in request.args:
        print(request.args['user'] + '\n' + request.args['pass'])
        #hash user and pass
        cursor.execute('select sID from staff where sUserName=%s and sPassword=%s;', (request.args['user'], request.args['pass']))
        sID = cursor.fetchone()[0]
        if sID is not None:
            token = utils.gen_token(32)
            cursor.execute('insert into tokens(sID,token,rank)values(%s,%s,1);', (sID, token))
            db.commit()
            return make_response(jsonify( { 'Token': token } ), 200)
    return make_response(jsonify( { 'Error:': 'Invalid Credentials' } ), 401)

@app.route('/login_admin', methods=['GET'])
def login_admin():
    if 'user' in request.args and 'pass' in request.args:
        print(request.args['user'] + '\n' + request.args['pass'])
        #Hash user and pass
        cursor.execute('select sID from admin where aUserName=%s and aPassword=%s', (request.args['user'], request.args['pass']))
        sID = cursor.fetchone()[0]
        if sID is not None:
            token = utils.gen_token(32)
            cursor.execute('insert into tokens(sID,token,rank)values(%s,%s,2);', (sID, token))
            db.commit()
            return make_response(jsonify( { 'Token': token } ), 200)
    return make_response(jsonify( { 'Error:': 'Invalid Credentials' } ), 401)

@app.route('/add_staff', methods=['POST'])
def add_staff():
    creds = auth(request.args.get('token'))
    if creds is not None and creds[1] == 2:
        dID = request.args.get('dID')
        sName = request.args.get('name')
        sUsername = request.args.get('user')
        sPass = request.args.get('pass')
        cursor.execute('select count(1) from staff where sUsername=%s',(sUsername,))
        cursor.execute('insert into staff (dID, sName, sUsername, sPass)values(%d, %s, %s, %s)',(dID, sName, sUsername, sPass))
        db.commit()
        return make_response(jsonify( { 'Message': f'User {sUsername} has been created' } ), 200)
    else:
        return make_response(jsonify( { 'Error:': 'Invalid Credentials' } ), 401)

@app.route('/add_admin', methods=['POST'])
def add_admin():
    creds = auth(request.args.get('token'))
    if creds is not None and creds[1] == 3:
        dID = request.args.get('dID')
        sName = request.args.get('name')
        sUsername = request.args.get('user')
        sPass = request.args.get('pass')
        cursor.execute('select count(1) from staff where sUsername=%s',(sUsername,))
        cursor.execute('insert into admin (dID, sName, sUsername, sPass)values(%d, %s, %s, %s)',(dID, sName, sUsername, sPass))
        db.commit()
        return make_response(jsonify( { 'Message': f'User {sUsername} has been created' } ), 200)
    else:
        return make_response(jsonify( { 'Error:': 'Invalid Credentials' } ), 401)

@app.route('/remove_staff', methods=['POST'])
def remove_staff():
    creds = auth(request.args.get('token'))
    if creds is not None and creds[1] == 2:
        cursor.execute('delete from staff where sID=%s DESC LIMIT 1',(creds[0],))
        db.commit()
        return make_response(jsonify( { 'Message': f'User {sID} has been removed from staff' } ), 200)
    else:
        return make_response(jsonify( { 'Error:': 'Invalid Credentials' } ), 401)

@app.route('/remove_admin', methods=['GET'])
def remove_admin():
    creds = auth(request.args.get('token'))
    if creds is not None and cerds[1] == 3:
        cursor.execute('delete DESC LIMIT 1 from admin where sID=%s',(creds[0],))
        db.commit()
        return make_response(jsonify( { 'Message': f'User {sID} has been removed from admin' } ), 200)
    else:
        return make_response(jsonify( { 'Error:': 'Invalid Credentials' } ), 401)

@app.route('/get_user', methods=['GET'])
def get_user():
    creds = auth(request.args.get('token'))
    if creds is not None:
        try:
            if creds[1] == 1:
                cursor.execute('select * from staff where sID=%s;', (creds[0],))
                user = cursor.fetchone()
                cursor.execute('select * from schedule where sID=%s;', (creds[0],))
                sched = cursor.fetchone()
            elif creds[1] == 2:
                sID = requet.args.get('sID')
                cursor.execute('select * from staff where sID=%s;', (sID,))
                user = cursor.fetchone()
                cursor.execute('select * from schedule where sID=%s;', (sID,))
                sched = cursor.fetchone()
            elif creds[1] == 3:
                sID = requet.args.get('sID')
                table = requet.args.get('table')
                cursor.execute('select * from %s where sID=%s;', (table,sID,))
                user = cursor.fetchone()
                cursor.execute('select * from schedule where sID=%s;', (sID,))
                sched = cursor.fetchone()
            if sched is None:
                sched = ''
            if user is not None:
                return make_response(jsonify( { 'UserData': str(user), 'Schedule': str(sched) } ), 200)
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)

@app.route('/update_user', methods=['POST'])
def update_user():
    if sID is not None:
        try:
            sID = auth(request.args.get('token'))
            arg = request.args.get('dID')
            dID = request.args.get('dep')
            cursor.execute('UPDATE user set dID=%s where sID=%s')
            #if arg is not None:
            arg = request.args.get('email')
            #if arg is not None:
            arg = request.args.get('name')
            #if arg is not None:
            db.commit()
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)
    else:
        return make_response(jsonify( { 'Response': 'Error. User not permittedd to do this.' }), 501)


@app.route('/reset_pass', methods=['POST'])
def reset_pass():
    sID = auth(request.args.get('token'))
    new_pass = request.args.get('pass')
    if sID is not None and new_pass is not none:
        try:
           #create hash and salt and store as  new_pass
           cursor.execute('UPDATE staff set sPassword=%s where sID=%s', (new_pass, sID))
           db.commit()
           return make_response(jsonify( { 'Response': 'Password has been reset.' }), 200)

        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)
    else:
        return make_response(jsonify( { 'Response': 'Error. User is not authorized to do this.' }), 501)


@app.route('/add_scheduled', methods=['POST'])
def add_schedule():
    if sID is not None:
        try:
        #code goes here
            sID = None
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)

@app.route('/remove_scheduled', methods=['POST'])
def remove_schedule():
    if sID is not None:
        try:
        #code goes here
            sID = None
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)

@app.route('/add_department', methods=['POST'])
def add_department():
    creds = auth(request.args.get('token'))
    if creds is not None and creds[1] == 2:
        try:
            dep = request.args.get('dep')
            cursor.execute('select dID from department where dName=%s', (dep, ))
            if cursor.fetchone() is not None:
                cursor.execute('insert into department (dName)values(%s)', (dep, ))
                return make_response(jsonify( { 'Response': 'Department has been added.' } ), 200)
            else:
                return make_response(jsonify( { 'Response': 'Department already exists' } ), 400)
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)

@app.route('/remove_department', methods=['POST'])
def remove_department():
    creds = auth(request.args.get('token'))
    if creds is not None and creds[1] == 2:
        try:
            dID = request.args.get('dID')
            cursor.execute('select dID from department where dID=%d', (dID, ))
            if cursor.fetchone() is not None:
                cursor.execute('delete from department where dName=%s', (dep, ))
                return make_response(jsonify( { 'Response': 'Department has been removed.' } ), 200)
            else:
                return make_response(jsonify( { 'Response': 'There was an error removing the department' } ), 501)
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)


if __name__ == "__main__":
    import logging
    logging.basicConfig(filename='_api.log',level=logging.DEBUG)
    app.run(debug=Debug, host=Host, port=Port)

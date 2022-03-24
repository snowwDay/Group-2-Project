from flask import Flask, request, redirect, jsonify
from db import *
from utils import *
from hasher import *

Debug=True
Host=''
Port=2000

app = Flask(__name__)
auth = HTTPBasicAuth()

def auth(args):
    if 'token' not in args:
        return false
    cursor.execute('select sID from tokens where token=%s;', (args['token']))
    if cursor.fetchone()[0]:
        return true
    return false

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/update-user', methods=['POST'])
def update_user():
    cursor.execute('select count(1) from staff where Username=%s and Password=%s;', (username, password))
    if cursor.fetchone()[0]:
        return cursor.fetchone()[0][0]
        ##Switch to saved sessions, and use sID
        #cursor.execute('select count(1) from Users where sID=%;', (sID))

@app.route('/login', methods=['GET'])
def login():
    if 'user' in request.args and 'pass' in request.args:
        print(request.args['user'] + '\n' + request.args['pass'])
        cursor.execute('select sID from staff where sUserName=%s and sPassword=%s;', (request.args['user'], request.args['pass']))
        if cursor.fetchone()[0]:
            token = gen_token(32)
            cursor.execute('insert into staff(sID,token);', (cursor.fetchone()[0][0], token))
            return make_response(jsonify( { 'Token': token } ), 200)
    return make_response(jsonify( { 'Error:': 'Invalid Credentials' } ), 401)
    
@app.route('/get-user', methods=['GET'])
@auth
def get_user():
    try:
        if len(request.args) < 2:
            abort(400)

        cursor.execute('select count(1) from staff where sID=%s;', (sID))
        if cursor.fetchone()[0]:
            return make_response(jsonify( { 'Data': str(cursor.fetchone()[0]) } ), 200)
    except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
        abort(400)

if __name__ == "__main__":
    import logging
    logging.basicConfig(filename='_api.log',level=logging.DEBUG)
    app.run(debug=Debug, host=Host, port=Port)

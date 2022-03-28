from flask import Flask, request, redirect, jsonify, make_response
from Db import *
from Utils import *
from Hasher import *

Debug=True
Host='137.184.96.25'
Port=2000

app = Flask(__name__)

def auth(arg):
    if arg is None:
        return -1
    cursor.execute('select sID from tokens where token=%s ORDER BY creationDate DESC LIMIT 1;', (arg,))
    sID = cursor.fetchone()[0]
    if sID is not None:
        return sID
    return -1


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/login', methods=['GET'])
def login():
    if 'user' in request.args and 'pass' in request.args:
        print(request.args['user'] + '\n' + request.args['pass'])
        cursor.execute('select sID from staff where sUserName=%s and sPassword=%s;', (request.args['user'], request.args['pass']))
        sID = cursor.fetchone()[0]
        if sID > -1:
            token = utils.gen_token(32)
            cursor.execute('insert into tokens(sID,token)values(%s,%s);', (sID, token))
            db.commit()
            return make_response(jsonify( { 'Token': token } ), 200)
    return make_response(jsonify( { 'Error:': 'Invalid Credentials' } ), 401)

@app.route('/get-user', methods=['GET'])
def get_user():
    sID = auth(request.args.get('token'))
    if sID is not None:
        try:
            cursor.execute('select * from staff where sID=%s;', (sID,))
            user = cursor.fetchone()
            cursor.execute('select * from schedule where sID=%s;', (sID,))
            sched = cursor.fetchone()
            if sched is None:
                sched = ''
            if user is not None:
                return make_response(jsonify( { 'UserData': str(user), 'Schedule': str(sched) } ), 200)
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DataError ) as err:
            print(err)

#@app.route('/update_user', methods=['POST'])
#def update_user():

#@app.route('/reset_pass', methods=['POST'])
#def reset_pass():

#@app.route('/add_scheduled', methods=['POST'])
#def add_scheduled():

#@app.route('/remove_scheduled', methods=['POST'])
#def remove_scheduled():

if __name__ == "__main__":
    import logging
    logging.basicConfig(filename='_api.log',level=logging.DEBUG)
    app.run(debug=Debug, host=Host, port=Port)

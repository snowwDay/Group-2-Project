from flask_httpauth import HTTPBasicAuth
from flask import Flask, request, redirect, jsonify
from db import *

Debug=True
Host=''
Port=2000

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    print(username + '\n' + password)
    cursor.execute('select count(1) from Users where Username=%s and Password=%s;', (username, password))
    if cursor.fetchone()[0]:
        return username
    return None

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
@auth.login_required
def update_user():
	cursor.execute('select count(1) from Users where Username=%s and Password=%s;', (username, password))
    if cursor.fetchone()[0]:
        info = cursor.fetchone()[0]
		##Switch to saved sessions, and use sID
	    #cursor.execute('select count(1) from Users where sID=%;', (sID))
		
@app.route('/get-user', methods=['GET'])
@auth.login_required
def get_user():
	cursor.execute('select count(1) from Users where Username=%s and Password=%s;', (username, password))
    if cursor.fetchone()[0]:
            return make_response(jsonify( { 'Data': str(cursor.fetchone()[0]) } ), 200)

if __name__ == "__main__":
    import logging
    logging.basicConfig(filename='/home/uploads/_up.log',level=logging.DEBUG)
    app.run(debug=Debug, host=Host, port=Port)

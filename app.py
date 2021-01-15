import uuid
from flask import Flask
from flask import request
from flask import jsonify 
from flask_cors import CORS 
app = Flask(__name__)
CORS(app)

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

def random_id_generator():
    return uuid.uuid4().hex[:6]
    

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        search_job= request.args.get('job')
        if search_username and search_job:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username and user['job'] == search_job:
                    subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()
        userToAdd['id'] = random_id_generator()
        users['users_list'].append(userToAdd)
        resp = jsonify(userToAdd)
        resp.status_code = 201
        #resp.status_code = 200 #optionally, you can always set a response code. 
        # 200 is the default code for a normal response
        return resp
    elif request.method == 'DELETE':
        # need to send whole user to the request
        userToDelete = request.get_json()
        users['users_list'].remove(userToDelete)
        resp = jsonify(success=True)
        #resp.status_code = 200 #optionally, you can always set a response code. 
        # 200 is the default code for a normal response
        return resp 

@app.route('/')
def hello_world():
    return 'Hello, World'
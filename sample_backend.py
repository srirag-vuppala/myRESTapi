from flask import request
from flask import Flask
app = Flask(__name__)

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

@app.route('/users/<id>')
def get_users(id):
    if id:
        for user in users['users_list']:
            if user['id'] == id:
                return user
        #if wrong user id is given to us return null {}
        return ({}) 
    return users

@app.route('/')
def hello_world():
    return 'Hello, World'
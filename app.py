from flask import Flask
import os
from flask_pymongo import PyMongo

mongo = PyMongo()
app = Flask(__name__)
print(os.environ.get('MONGO_URI'))
app.config['MONGO_URI']="mongodb+srv://nischaya:pass@cluster0-hoqge.mongodb.net/test?retryWrites=true&w=majority"
mongo.init_app(app)

@app.route('/')
def index():
    user_collection=mongo.db.users
    user_collection.insert({'name' : 'Apurv', 'language' : 'JavaScript'})
    return "<h1>Added a user</h1>"

@app.route('/find')
def find():
    user_collection = mongo.db.users
    user = user_collection.find_one({'name' : 'Apoorva'})
    return f'User: {user["name"]} <br>Language: {user["language"]}'

@app.route('/update')
def update():
    user_collection=mongo.db.users
    user = user_collection.find_one({'name': 'Nischaya'})
    user['language']='Python'
    user_collection.save(user)
    return "User updated"

@app.route('/delete')
def delete():
    user_collection=mongo.db.users
    user=user_collection.find_one({'name':'Anthony'})
    user_collection.remove(user)
    return "User Removed"

if(__name__=="__main__"):
    app.run(debug=True)
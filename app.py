from flask import Flask
import os
from flask_pymongo import PyMongo
import collections

mongo = PyMongo()
app = Flask(__name__)
app.config['MONGO_URI']="mongodb://localhost:27017/thesocialcomment"
mongo.init_app(app)

def logic(following, subFollowing):
    subsFinal = []
    for sub in subFollowing:
        subsFinal.append(list(set(sub) - set(following)))
    freqDic = dict(collections.Counter([x for sublist in subsFinal for x in sublist]))
    return freqDic

@app.route('/recommend')
def recommend():
    user_collection = mongo.db.user
    user = user_collection.find_one({'name' : 'Nivesh Singh Chauhan'})
    following = []
    for follow in user["following"]:
        following.append(user_collection.find_one({'_id':follow}))
    subs = []
    for users in following:
        print(users)
        subFollowing = []
        for follow in users["following"]:
            subFollowing.append(user_collection.find_one({'_id':follow}))
        print(logic(following,subFollowing))
        subs.append(subFollowing)
    print("subs",subs)
    return f'User: {user["name"]} <br>followers:{following[2]["name"]}'

if __name__=="__main__":
    app.run(debug=True)
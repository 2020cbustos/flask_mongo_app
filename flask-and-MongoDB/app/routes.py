import os
from app import app
from flask import render_template, request, redirect

#username = "period8"
#events = [
        #{"event":"First Day of Classes", "date":"2019-08-21"},
        #{"event":"Winter Break", "date":"2019-12-20"},
        #{"event":"Finals Begin", "date":"2019-12-01"}
    #]


from flask_pymongo import PyMongo

# name of database on mongo db where all the data is sent
app.config['MONGO_DBNAME'] = 'test'

# URI of database (including the specific username and password)
app.config['MONGO_URI'] = 'mongodb+srv://admin:2uJv8gjTufj2gXOn@cluster0-lkr02.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)

# INDEX
@app.route('/index')
def index():
    events = mongo.db.events
    #query to find everything in events
    events = list(events.find({}))
    print(events)
    #this renders HTML - go to the index.html file
    return render_template('index.html', events = events)


# CONNECT TO DB, ADD DATA
@app.route('/add')
def add():
    # connect to the database
    test = mongo.db.test
    # insert new data
    test.insert({"name":"last day of school"})
    # return a message to the user
    return "Added data to database"

@app.route('/deleteAll')
def deleteAll():
    #connect to the database
    events = mongo.db.events
    #run delete many to clear data
    events.delete_many({})
    #this renders HTML - go to the deleteAll.html file
    return render_template("deleteAll.html")

@app.route('/input')
def input():
    #this renders HTML - go to the input.html file
    return render_template('input.html')

@app.route('/results', methods = ['Get','Post'])
def results():
    #dictionary request
    userdata = dict(request.form)
    event_name = userdata['event_name']
    event_date = userdata['event_date']
    event_type = userdata['event_type']
    #connect to DB
    events = mongo.db.events
    #dict insertion as data display
    events.insert({'name':event_name, 'date':event_date, 'type':event_type})
    #redirect results directly to index
    return redirect ("/index")

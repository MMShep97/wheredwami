import pyrebase
import os
# from dotenv import load_dotenv
# load_dotenv

# API_KEY = os.getenv('API_KEY')

apiKey = ''
authDomain = ''
databaseURL = ''
projectId = ''
storageBucket = ''
messagingSenderId = ''
appId = ''

config = {
    apiKey: "AIzaSyDefOb81ny8uUk9fEjNMFHKpb8YwZtr6xg",
    authDomain: "wheredwami.firebaseapp.com",
    databaseURL: "https://wheredwami.firebaseio.com",
    projectId: "wheredwami",
    storageBucket: "wheredwami.appspot.com",
    messagingSenderId: "696688358809",
    appId: "1:696688358809:web:e0438259f46f52e4dd4f08"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

data = {
    "name" : "Morty"
}

results = database.child('/').update({"poster1": True})
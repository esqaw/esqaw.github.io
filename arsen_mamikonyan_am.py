from flask import Flask
from flask import render_template
import yaml


app = Flask(__name__)

@app.route('/')
def index():
    projects = [
      {
        'title': 'Hygir',
        'description': 'Help people write in Armenian',
        'url': 'http://hygir.com',
      }
    ]
    overview_dict = yaml.load(open('knowledge/overview.yml', 'r'))
    profiles = overview_dict['Social Profiles']
    interests = overview_dict['Interests']
    return render_template('index.html',
                           interests=interests,
                           profiles=profiles,
                           projects=projects)

@app.route('/reading/')
def reading():
    books_dict = yaml.load(open('knowledge/books.yml', 'r'))
    reading = books_dict['Reading']
    recomendations = books_dict['Recommend']
    still_reading = books_dict['Still Reading']
    return render_template('reading.html',
                           title='Reading',
                           books={'Currently Reading': reading,
                                  'Still Reading': still_reading,
                                  'I recommend': recomendations})

@app.route('/reading_history/')
def reading_history():
    books_dict = yaml.load(open('knowledge/books.yml', 'r'))
    all_books = books_dict['Reading History']
    return render_template('reading.html',
                           title='Books I Have Read',
                           books={'Reading History (2015)': all_books})


@app.route('/photos/')
def photos():
    return render_template('photos.html',
                           title='Photos',
                           photos={})

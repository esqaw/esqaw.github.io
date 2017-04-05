from flask import Flask
from flask import render_template
import yaml


app = Flask(__name__)


@app.route('/')
def index():
    projects = [
      {
        'title': 'Machine Learning Course in Yerevan',
        'description': 'Machine Leraning Course, to make people ready to work in the industry doing ML.',
        'url': 'ml_afternoon/',
      },
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
                           block_to_books={'Currently Reading': reading,
                                           'Still Reading': still_reading,
                                           'I recommend': recomendations})


@app.route('/reading_history/')
def reading_history():
    books_dict = yaml.load(open('knowledge/books.yml', 'r'))
    all_books = books_dict['Reading History']
    return render_template('reading.html',
                           title='Books I Have Read',
                           block_to_books={
                              'Reading History (2015-present)': all_books})


@app.route('/photos/')
def photos():
    return render_template('photos.html',
                           title='Photos',
                           photos={})


@app.route('/ml_afternoon/')
def ml_afternoon():
    return render_template('ml_lectures.html',
                           title='Machine Learning Course',
                           lectures={'0. Introduction': '../ml_lectures/0_introduction/',
                                     '1. Introduction': '../ml_lectures/1_regression/'})


@app.route('/ml_lectures/<string:lecture_name>/')
def ml_lectures(lecture_name):
    return render_template('ml_lectures/%s.html' % lecture_name)

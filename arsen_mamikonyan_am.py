from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    interests = [{
        'name': 'Photography',
        'url': 'http://ppd.arsen.mamikonyan.am/',
      },
      {
        'name': 'Cooking',
        'url': 'http://cook.arsen.mamikonyan.am/',
      },
      {
        'name': 'Soccer',
      },
      {
        'name': '3d printing',
      },
      {
        'name': 'Scuba Diving',
      }
    ]
    profiles = [
      {
        'service': 'email',
        'url': 'mailto:arsen@mamikonyan.am',
      },
      {
        'service': 'linkedin',
        'url': 'https://www.linkedin.com/in/mamikonyana',
      },
      {
        'service': 'facebook',
        'url': 'https://www.facebook.com/arsen.mamikonyan',
      },
      {
        'service': 'twitter',
        'url': 'https://twitter.com/mamikonyana',
      },
      {
        'service': 'github',
        'url': 'https://github.com/mamikonyana'
      }
    ]
    projects = [
      {
        'title': 'Hygir',
        'description': 'Help people write in Armenian',
        'url': 'http://hygir.com',
      }
    ]
    return render_template('index.html',
                           interests=interests,
                           profiles=profiles,
                           projects=projects)

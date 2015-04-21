from flask.ext.frozen import Freezer
from arsen_mamikonyan_am import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()

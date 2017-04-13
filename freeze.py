import os
from flask_frozen import Freezer
from arsen_mamikonyan_am import app

freezer = Freezer(app)


@freezer.register_generator
def ml_afternoon():
    path = os.path.join(app.root_path, 'templates/ml_afternoon/')
    files = next(os.walk(path))[2]
    for _file in files:
        if _file.endswith('.html'):
            print(_file)
            yield {'lecture_name': os.path.splitext(_file)[0]}


@freezer.register_generator
def ml_evening():
    path = os.path.join(app.root_path, 'templates/ml_evening/')
    files = next(os.walk(path))[2]
    for _file in files:
        if _file.endswith('.html'):
            print(_file)
            yield {'lecture_name': os.path.splitext(_file)[0]}

if __name__ == '__main__':
    freezer.freeze()

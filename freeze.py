import os
from flask_frozen import Freezer
from arsen_mamikonyan_am import app

freezer = Freezer(app)


@freezer.register_generator
def ml_lectures():
    path = os.path.join(app.root_path, 'ml_lectures')
    files = next(os.walk(path))[2]
    for _file in files:
        if _file.endswith('.html'):
            yield {"lecture_name": _file.strip('.html')}

if __name__ == '__main__':
    freezer.freeze()

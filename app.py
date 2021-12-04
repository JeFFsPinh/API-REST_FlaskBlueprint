from flask import Flask

from blueprints import dono
from blueprints import animal

app = Flask(__name__)

dono.init_app(app)
animal.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
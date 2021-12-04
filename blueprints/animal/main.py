from blueprints.animal import view
from flask import Blueprint
from flask.app import Flask

bp_animal = Blueprint('animal', __name__, url_prefix='/animal')
bp_animal.add_url_rule('/', view_func=view.listar_animais, methods=["GET"])
bp_animal.add_url_rule('/', view_func=view.adicionar_animal, methods=["POST"])


def init_app(app: Flask):
    app.register_blueprint(bp_animal)
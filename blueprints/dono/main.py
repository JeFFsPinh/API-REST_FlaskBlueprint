from blueprints.dono import view
from flask import Blueprint
from flask.app import Flask

bp_dono = Blueprint('dono', __name__, url_prefix='/dono')
bp_dono.add_url_rule('/', view_func=view.listar_donos, methods=["GET"])
bp_dono.add_url_rule('/<string:nome>', view_func=view.info_dono, methods=["GET"])
bp_dono.add_url_rule('/', view_func=view.adicionar_dono, methods=["POST"])


def init_app(app: Flask):
    app.register_blueprint(bp_dono)
from blueprints.animal import view
from flask import Blueprint
from flask.app import Flask

bp_animal = Blueprint('animal', __name__, url_prefix='/animal')
bp_animal.add_url_rule('/', view_func=view.listar_animais, methods=["GET"])
bp_animal.add_url_rule('/<string:nome>', view_func=view.info_animal_nome, methods=["GET"])
bp_animal.add_url_rule('/<int:Id>', view_func=view.info_animal_Id, methods=["GET"])
bp_animal.add_url_rule('/', view_func=view.adicionar_animal, methods=["POST"])
bp_animal.add_url_rule('/<int:Id>', view_func=view.atualizar_animal, methods=["PUT"])
bp_animal.add_url_rule('/<int:Id>', view_func=view.deletar_animal, methods=["DELETE"])


def init_app(app: Flask):
    app.register_blueprint(bp_animal)
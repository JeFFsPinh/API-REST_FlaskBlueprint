from blueprints.database import repositorio
from blueprints.Models import Dono
from flask import request, jsonify


def adicionar_dono():
    cadastro_dono = request.json # criação de variável para manipulação do request.json

    for item, valor in cadastro_dono.items():  # tratamento nos dados que estão no request.json
        cadastro_dono[item] = valor.lower().strip()

    if not cadastro_dono.get("nome"): # proibição do cadastro sem o nome
        return jsonify({"error": "O nome é obrigatório"}), 422

    if not cadastro_dono.get("cpf"): # proibição do cadastro sem o cpf
        return jsonify({"error": "O cpf é obrigatório"}), 422

    usuario = Dono(cadastro_dono.get("nome"), cadastro_dono.get("cpf"))

    for i in repositorio.listar_donos(): # validação e proibição do cadastro de um usuário que já foi cadastrado anteriormente
        if usuario.nome == i.get("nome"):
            return jsonify({"error": "O usuário já existe"}), 422

    repositorio.adicionar_dono(usuario) # inserção dos dados
    return jsonify("Cadastro feito!"), 201

def listar_donos():    
    return jsonify({"cadastro_dono": repositorio.listar_donos()}), 200

def info_dono(nome: str):
    return jsonify(repositorio.info_dono(nome)), 200

from blueprints.Models import Animal
from blueprints.database import repositorio
from flask import request, jsonify


def adicionar_animal():
    cadastro_animal = request.json # criação de variável para manipulação do request.json

    for item, valor in cadastro_animal.items(): # tratamento nos dados que estão no request.json
            cadastro_animal[item] = valor.lower().strip()

    if not cadastro_animal.get("dono"): # proibição do cadastro sem o nome do dono
            return jsonify({"error": "O nome do dono é obrigatório"}), 422

    pet = Animal(cadastro_animal.get("tipo"), cadastro_animal.get("raça"), cadastro_animal.get("dono"))

    for i in repositorio.listar_donos():  # validação e proibição do cadastro de um animal com o nome do dono diferente ou inexistente na db_dono
        if pet.dono == i.get("nome"):
            repositorio.adicionar_animal(pet)
            return jsonify("Cadastro feito!"), 201
    return jsonify({"error": "Dono não encontrado"}), 422 # retorno do erro caso o dono não existir na db_dono


def listar_animais():
    return jsonify({"cadastro_animais": repositorio.listar_animais()}), 200
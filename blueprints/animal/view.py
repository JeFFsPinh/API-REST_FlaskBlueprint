from typing import Dict
from blueprints.Models import Animal
from blueprints.database import repositorio
from flask import request, jsonify



'''def validação_dados_animal(request):
    aux: Dict = request
    for item, valor in aux.items(): # tratamento nos dados que estão no request.json
            aux[item] = valor.lower().strip()

    if not aux.get("dono"): # proibição do cadastro sem o nome do dono
            return jsonify({"error": "O nome do dono é obrigatório"}), 422

    if not aux.get("tipo"): # proibição do cadastro sem o tipo do animal
            return jsonify({"error": "Tipo do animal é obrigatório"}), 422

    if not aux.get("raça"): # proibição do cadastro sem o nome da raça
            return jsonify({"error": "O nome da raça é obrigatório"}), 422

    for i in repositorio.listar_donos():  # validação e proibição do cadastro de um animal com o nome do dono diferente ou inexistente na db_dono
        if aux.get("dono") == i.get("nome"):
            if request.method == "POST":
                pet = Animal(repositorio.gerar_id_animal() ,aux.get("tipo"), aux.get("raça"), aux.get("dono"))
                repositorio.adicionar_animal(pet)
                return jsonify("Cadastro feito!"), 201
            # if request.method == "PUT":     
        else:
            return jsonify({"error": "Dono não encontrado"}), 422'''


def adicionar_animal():
    cadastro_animal = request.json # criação de variável para manipulação do request.json

    for item, valor in cadastro_animal.items(): # tratamento nos dados que estão no request.json
            cadastro_animal[item] = valor.lower().strip()

    if not cadastro_animal.get("dono"): # proibição do cadastro sem o nome do dono
            return jsonify({"error": "O nome do dono é obrigatório"}), 422

    if not cadastro_animal.get("tipo"): # proibição do cadastro sem o tipo do animal
            return jsonify({"error": "Tipo do animal é obrigatório"}), 422

    if not cadastro_animal.get("raça"): # proibição do cadastro sem o nome da raça
            return jsonify({"error": "O nome da raça é obrigatório"}), 422

    for i in repositorio.listar_donos():  # validação e proibição do cadastro de um animal com o nome do dono diferente ou inexistente na db_dono
        if cadastro_animal.get("dono") == i.get("nome"):
                pet = Animal(repositorio.gerar_id_animal(), cadastro_animal.get("tipo"), cadastro_animal.get("raça"), cadastro_animal.get("dono"))
                repositorio.adicionar_animal(pet)
                return jsonify("Cadastro feito!"), 201
    return jsonify({"error": "Dono não encontrado"}), 422 # retorno do erro caso o dono não existir na db_dono


def atualizar_animal(Id: int):
    cadastro_animal = request.json # criação de variável para manipulação do request.json

    for item, valor in cadastro_animal.items(): # tratamento nos dados que estão no request.json
            cadastro_animal[item] = valor.lower().strip()

    if not cadastro_animal.get("dono"): # proibição do cadastro sem o nome do dono
            return jsonify({"error": "O nome do dono é obrigatório"}), 422

    if not cadastro_animal.get("tipo"): # proibição do cadastro sem o tipo do animal
            return jsonify({"error": "Tipo do animal é obrigatório"}), 422

    if not cadastro_animal.get("raça"): # proibição do cadastro sem o nome da raça
            return jsonify({"error": "O nome da raça é obrigatório"}), 422

    for i in repositorio.listar_donos():  # validação e proibição do cadastro de um animal com o nome do dono diferente ou inexistente na db_dono
        if cadastro_animal.get("dono") == i.get("nome"):
                pet = Animal(Id, cadastro_animal.get("tipo"), cadastro_animal.get("raça"), cadastro_animal.get("dono"))
                repositorio.atualizar_animal(pet)
                return jsonify("Cadastro atualizado!"), 201
    return jsonify({"error": "Dono não encontrado"}), 422 # retorno do erro caso o dono não existir na db_dono


def listar_animais():
    return jsonify({"cadastros": repositorio.listar_animais()}), 200

def info_animal_nome(nome: str):
    return jsonify(repositorio.info_animal_nome(nome)), 200

def info_animal_Id(Id: int):
    return jsonify(repositorio.info_animal_Id(Id)), 200

def deletar_animal(Id: int):
    repositorio.deletar_animal(Id)
    return jsonify(), 204
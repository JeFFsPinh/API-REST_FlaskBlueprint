from typing import Dict, List
from blueprints.Models import Animal, Dono
from flask import jsonify

db_dono: List[Dict[str, str]] = []
db_animal: List[Dict[str, str]] = []
Id_dono: int = 0
Id_animal: int = 0

class repositorio():
    @staticmethod
    def adicionar_dono(pet: Dono):
        db_dono.append(pet.to_dict())

    @staticmethod
    def listar_donos():
        return db_dono

    # @staticmethod
    # def info_dono_nome(nome: str):
    #     aux = filter(lambda dono: dono["nome"] == nome, db_dono)
    #     return [dono for dono in aux]

    @staticmethod
    def info_dono_Id(Id: int):
        for i in db_dono:
            if Id == i.get("id"):
                return i
            
        return jsonify({"erro": "usuário não encontrado"})

    @staticmethod
    def gerar_id_dono():
        global Id_dono
        Id = Id_dono
        Id_dono += 1
        return Id

    @staticmethod
    def atualizar_dono(usuario: Dono):
        global db_dono
        db_dono = [usuario.to_dict() if dono.get("id") == usuario.Id else dono for dono in db_dono] 

    @staticmethod
    def deletar_dono(Id: int):
        for i in db_dono:
            if Id == i.get("id"):
                return db_dono.remove(i)
    
    @staticmethod
    def adicionar_animal(animal: Animal):
        db_animal.append(animal.to_dict())

    @staticmethod
    def listar_animais():
        return db_animal

    @staticmethod
    def info_animal(nome: str):
        aux = filter(lambda animal: animal["dono"] == nome, db_animal)
        return [animal for animal in aux]

    @staticmethod
    def gerar_id_animal():
        global Id_animal
        Id = Id_animal
        Id_animal += 1
        return Id
        
    # @staticmethod
    # def info_animal_nome(dono: str):
    #     aux = filter(lambda animal: animal["dono"] == dono, db_animal)
    #     return [animal for animal in aux]

    @staticmethod
    def info_animal_Id(Id: int):
        for i in db_animal:
            if Id == i.get("id"):
                return i
            
        return {"erro": "dono não encontrado"}

    @staticmethod
    def atualizar_animal(pet: Animal):
        global db_animal
        db_animal = [pet.to_dict() if animal.get("id") == pet.Id else animal for animal in db_animal] 

    @staticmethod
    def deletar_animal(Id: int):
        for i in db_animal:
            if Id == i.get("id"):
                return db_animal.remove(i)

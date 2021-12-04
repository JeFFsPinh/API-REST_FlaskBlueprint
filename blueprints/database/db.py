from typing import Dict, List

from blueprints.Models import Animal, Dono


db_dono: List[Dict[str, str]] = []
db_animal: List[Dict[str, str]] = []

class repositorio():
    @staticmethod
    def adicionar_dono(dono: Dono):
        db_dono.append(dono.to_dict())

    @staticmethod
    def listar_donos():
        return db_dono

    @staticmethod
    def info_dono(nome: str):
        aux = filter(lambda dono: dono["nome"] == nome, db_dono)
        return [dono for dono in aux]

    @staticmethod
    def adicionar_animal(animal: Animal):
        db_animal.append(animal.to_dict())

    @staticmethod
    def listar_animais():
        return db_animal

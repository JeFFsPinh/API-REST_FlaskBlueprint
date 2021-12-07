from typing import Dict, Any

class Dono():
    def __init__(self, Id: int, nome: str, cpf: str):
        self.Id = Id
        self.nome = nome
        self.cpf = cpf

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.Id,
            "nome": self.nome,
            "cpf": self.cpf
        }
from typing import Dict, Any

class Dono():
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    def to_dict(self) -> Dict[str, Any]:
        return {
            "nome": self.nome,
            "cpf": self.cpf
        }
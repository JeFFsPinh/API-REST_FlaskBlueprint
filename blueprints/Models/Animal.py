from typing import Dict, Any

class Animal():
    def __init__(self, Id: int, tipo: str, raça: str, dono: str):
        self.Id = Id
        self.tipo = tipo
        self.raça = raça
        self.dono = dono


    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.Id,
            "tipo": self.tipo,
            "raça": self.raça,
            "dono": self.dono
        }
        

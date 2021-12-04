from typing import Dict, Any

class Animal():
    def __init__(self, tipo: str, raça: str, dono: str):
        self.tipo = tipo
        self.raça = raça
        self.dono = dono

    def to_dict(self) -> Dict[str, Any]:
        return {
            "tipo": self.tipo,
            "raça": self.raça,
            "dono": self.dono
        }

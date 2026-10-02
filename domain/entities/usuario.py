from dataclasses import dataclass


@dataclass
class Usuario:

    id: int | None
    nome: str
    cpf: str

from pydantic import BaseModel


class UsuarioCreateDTO(BaseModel):
    nome: str
    cpf: str


class UsuarioResponseDTO(BaseModel):
    id: int
    nome: str
    cpf: str

    class Config:
        from_attributes = True
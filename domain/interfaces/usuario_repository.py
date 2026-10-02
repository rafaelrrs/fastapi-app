from abc import ABC, abstractmethod

from domain.entities.usuario import Usuario


class UsuarioRepository(ABC):

    @abstractmethod
    def criar(self, usuario: Usuario) -> Usuario:
        pass

    @abstractmethod
    def buscar_por_id(self, usuario_id: int) -> Usuario | None:
        pass

    @abstractmethod
    def buscar_por_cpf(self, cpf: str) -> Usuario | None:
        pass

    @abstractmethod
    def listar(self) -> list[Usuario]:
        pass

    @abstractmethod
    def atualizar(self, usuario: Usuario) -> Usuario:
        pass

    @abstractmethod
    def excluir(self, usuario_id: int) -> None:
        pass
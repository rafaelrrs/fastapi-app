from domain.entities.usuario import Usuario
from domain.interfaces.usuario_repository import (
    UsuarioRepository
)

from application.factories.usuario_factory import (
    UsuarioFactory
)

from application.strategies.cpf_strategy import (
    CPFValidationStrategy
)

from infrastructure.adapters.cpf_adapter import (
    CPFAdapter
)


class UsuarioService:

    def __init__(
        self,
        repository: UsuarioRepository,
        cpf_strategy: CPFValidationStrategy
    ):
        self.repository = repository
        self.cpf_strategy = cpf_strategy

    def criar(
        self,
        nome: str,
        cpf: str
    ) -> Usuario:

        cpf = CPFAdapter.normalize(cpf)

        if not self.cpf_strategy.validate(cpf):
            raise ValueError(
                "CPF inválido"
            )

        usuario_existente = (
            self.repository.buscar_por_cpf(cpf)
        )

        if usuario_existente:
            raise ValueError(
                "CPF já cadastrado"
            )

        usuario = UsuarioFactory.create(
            nome=nome,
            cpf=cpf
        )

        return self.repository.criar(usuario)

    def buscar_por_id(
        self,
        usuario_id: int
    ) -> Usuario:

        usuario = (
            self.repository
            .buscar_por_id(usuario_id)
        )

        if not usuario:
            raise ValueError(
                "Usuário não encontrado"
            )

        return usuario

    def listar(self) -> list[Usuario]:

        return self.repository.listar()

    def atualizar(
        self,
        usuario_id: int,
        nome: str,
        cpf: str
    ) -> Usuario:

        usuario = self.buscar_por_id(
            usuario_id
        )

        cpf = CPFAdapter.normalize(cpf)

        if not self.cpf_strategy.validate(cpf):
            raise ValueError(
                "CPF inválido"
            )

        usuario.nome = nome.strip()
        usuario.cpf = cpf

        return self.repository.atualizar(
            usuario
        )

    def excluir(
        self,
        usuario_id: int
    ):

        self.buscar_por_id(usuario_id)

        self.repository.excluir(usuario_id)
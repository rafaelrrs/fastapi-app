from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from domain.entities.usuario import Usuario

from domain.interfaces.usuario_repository import (
    UsuarioRepository
)

from infrastructure.database.database import Base


class UsuarioModel(Base):

    __tablename__ = "usuarios"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    nome = Column(
        String(100),
        nullable=False
    )

    cpf = Column(
        String(11),
        unique=True,
        nullable=False,
        index=True
    )


class SqlAlchemyUsuarioRepository(
    UsuarioRepository
):

    def __init__(
        self,
        db: Session
    ):
        self.db = db

    def _to_entity(
        self,
        model: UsuarioModel
    ) -> Usuario:

        return Usuario(
            id=model.id,
            nome=model.nome,
            cpf=model.cpf
        )

    def _to_model(
        self,
        usuario: Usuario
    ) -> UsuarioModel:

        return UsuarioModel(
            id=usuario.id,
            nome=usuario.nome,
            cpf=usuario.cpf
        )

    def criar(
        self,
        usuario: Usuario
    ) -> Usuario:

        model = self._to_model(
            usuario
        )

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return self._to_entity(model)

    def buscar_por_id(
        self,
        usuario_id: int
    ) -> Usuario | None:

        model = self.db.query(
            UsuarioModel
        ).filter(
            UsuarioModel.id == usuario_id
        ).first()

        if not model:
            return None

        return self._to_entity(model)

    def buscar_por_cpf(
        self,
        cpf: str
    ) -> Usuario | None:

        model = self.db.query(
            UsuarioModel
        ).filter(
            UsuarioModel.cpf == cpf
        ).first()

        if not model:
            return None

        return self._to_entity(model)

    def listar(self) -> list[Usuario]:

        models = self.db.query(
            UsuarioModel
        ).all()

        return [
            self._to_entity(model)
            for model in models
        ]

    def atualizar(
        self,
        usuario: Usuario
    ) -> Usuario:

        model = self.db.query(
            UsuarioModel
        ).filter(
            UsuarioModel.id == usuario.id
        ).first()

        if not model:
            raise ValueError(
                "Usuário não encontrado"
            )

        model.nome = usuario.nome
        model.cpf = usuario.cpf

        self.db.commit()
        self.db.refresh(model)

        return self._to_entity(model)

    def excluir(
        self,
        usuario_id: int
    ) -> None:

        model = self.db.query(
            UsuarioModel
        ).filter(
            UsuarioModel.id == usuario_id
        ).first()

        if not model:
            raise ValueError(
                "Usuário não encontrado"
            )

        self.db.delete(model)
        self.db.commit()
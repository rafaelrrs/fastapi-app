from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from infrastructure.database.database import get_db

from infrastructure.repositories.usuario_repository import (
    SqlAlchemyUsuarioRepository
)

from application.services.usuario_service import (
    UsuarioService
)

from application.strategies.cpf_strategy import (
    SimpleCPFValidationStrategy
)

from application.dto.usuario_dto import (
    UsuarioCreateDTO,
    UsuarioResponseDTO
)


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)


def get_usuario_service(
    db: Session = Depends(get_db)
) -> UsuarioService:

    repository = SqlAlchemyUsuarioRepository(
        db
    )

    strategy = SimpleCPFValidationStrategy()

    return UsuarioService(
        repository=repository,
        cpf_strategy=strategy
    )


@router.post(
    "",
    response_model=UsuarioResponseDTO
)
def criar_usuario(
    dados: UsuarioCreateDTO,
    service: UsuarioService = Depends(
        get_usuario_service
    )
):

    try:

        return service.criar(
            nome=dados.nome,
            cpf=dados.cpf
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.get(
    "",
    response_model=list[UsuarioResponseDTO]
)
def listar_usuarios(
    service: UsuarioService = Depends(
        get_usuario_service
    )
):

    return service.listar()


@router.get(
    "/{usuario_id}",
    response_model=UsuarioResponseDTO
)
def buscar_usuario(
    usuario_id: int,
    service: UsuarioService = Depends(
        get_usuario_service
    )
):

    try:
        return service.buscar_por_id(
            usuario_id
        )

    except ValueError as error:

        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.put(
    "/{usuario_id}",
    response_model=UsuarioResponseDTO
)
def atualizar_usuario(
    usuario_id: int,
    dados: UsuarioCreateDTO,
    service: UsuarioService = Depends(
        get_usuario_service
    )
):

    try:

        return service.atualizar(
            usuario_id=usuario_id,
            nome=dados.nome,
            cpf=dados.cpf
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.delete(
    "/{usuario_id}"
)
def excluir_usuario(
    usuario_id: int,
    service: UsuarioService = Depends(
        get_usuario_service
    )
):

    try:

        service.excluir(usuario_id)

        return {
            "message": "Usuário excluído"
        }

    except ValueError as error:

        raise HTTPException(
            status_code=404,
            detail=str(error)
        )
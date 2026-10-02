from fastapi import FastAPI

from infrastructure.database.database import (
    Base,
    engine
)

from infrastructure.repositories.usuario_repository import (
    UsuarioModel
)

from presentation.routers.usuario_router import router


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="Usuario API",
    version="1.0.0"
)


app.include_router(router)
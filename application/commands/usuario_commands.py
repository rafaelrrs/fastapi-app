class CriarUsuarioCommand:

    def __init__(
        self,
        nome: str,
        cpf: str
    ):
        self.nome = nome
        self.cpf = cpf


class AtualizarUsuarioCommand:

    def __init__(
        self,
        usuario_id: int,
        nome: str,
        cpf: str
    ):
        self.usuario_id = usuario_id
        self.nome = nome
        self.cpf = cpf


class ExcluirUsuarioCommand:

    def __init__(
        self,
        usuario_id: int
    ):
        self.usuario_id = usuario_id
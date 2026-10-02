from domain.entities.usuario import Usuario


class UsuarioFactory:

    @staticmethod
    def create(
        nome: str,
        cpf: str
    ) -> Usuario:

        return Usuario(
            id=None,
            nome=nome.strip(),
            cpf=cpf
        )
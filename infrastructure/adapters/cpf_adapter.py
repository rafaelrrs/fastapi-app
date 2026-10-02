class CPFAdapter:

    @staticmethod
    def normalize(cpf: str) -> str:

        return (
            cpf
            .replace(".", "")
            .replace("-", "")
            .replace(" ", "")
        )
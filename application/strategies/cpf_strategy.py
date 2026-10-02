from abc import ABC, abstractmethod


class CPFValidationStrategy(ABC):

    @abstractmethod
    def validate(self, cpf: str) -> bool:
        pass


class SimpleCPFValidationStrategy(
    CPFValidationStrategy
):

    def validate(self, cpf: str) -> bool:

        if len(cpf) != 11:
            return False

        if not cpf.isdigit():
            return False

        return True
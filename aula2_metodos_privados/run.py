class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.cpf = cpf

    def apresentar(self):
        print(f'ola! Minha altura - {self.altura}')
        self.__coletar_documento()

    def __coletar_documento(self):
        print(f'Meu documento - {self.cpf}')
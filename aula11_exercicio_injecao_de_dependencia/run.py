class ConectorBancoDeDados:
    def __init__(self) -> None:
        self.connection = None

    def conectar_ao_banco(self) -> None:
        self.connection = True


class RepositorioDeBanco:
    def __init__(self, conexao: ConectorBancoDeDados) -> None:
        self.__conexao = conexao

    def buscar_dados(self) -> list:
        if self.__conexao.connection:
            return [1, 2, 3, 4, 5]
        return None
        

class RegraDeNegocio:
    def __init__(self, repositorio: RepositorioDeBanco) -> None:
        self.__repositorio = repositorio

    def calcular_resultados(self) -> None:
        dados = self.__repositorio.buscar_dados()
        if not dados:
            print('Dados não encontrados. Verifique sua conexão com o banco')
        else:
            resposta = 0
            for dado in dados:
                resposta += dado
            print(f'O resultado é: {resposta}')


conn = ConectorBancoDeDados()
conn.conectar_ao_banco()

repositorio = RepositorioDeBanco(conn)
regra = RegraDeNegocio(repositorio)

regra.calcular_resultados()
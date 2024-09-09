class MinhaClasse:

    estatico = 'lhama'

    def __init__(self, estado) -> None:
        self.__estado = estado

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

MinhaClasse.estatico = 'programador'
obj1.estatico = 'OlaMundo'

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)
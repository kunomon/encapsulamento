class Pessoa:
    def __init__(self, nome, sobrenome):
        self._nome = nome
        self._sobrenome = sobrenome

    @property
    def nome(self):
        return f'{self._nome} {self._sobrenome}'
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = str(novo_nome)

pessoa1 = Pessoa('Sérgio', 'Carvalho')
print(pessoa1.nome)

pessoa1.nome = 'Gabriel'
print(pessoa1.nome)
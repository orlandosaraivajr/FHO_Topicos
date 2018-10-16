class Pessoa:
    def __init__(self, nome=None):
        self.nome = nome

class PessoaFisica(Pessoa):
    def __init__(self, nome=None, cpf=None):
        self.nome = nome
        self.cpf = cpf

class PessoaJuridica(Pessoa):
    def __init__(self, nome=None, cnpj=None):
        self.nome = nome
        self.cnpj = cnpj
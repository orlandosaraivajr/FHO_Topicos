import re
mascara = '[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}'
validador_cpf = re.compile(mascara)


class Pessoa:
    def __init__(self, nome=None):
        self.nome = nome

class PessoaFisica(Pessoa):
    def __init__(self, nome=None, cpf=None):
        Pessoa.__init__(self, nome)
        if validador_cpf.match(cpf):
            self.cpf = cpf
        else:
            self.cpf = None

class PessoaJuridica(Pessoa):
    def __init__(self, nome=None, cnpj=None):
        Pessoa.__init__(self, nome)
        self.nome = nome
        self.cnpj = cnpj
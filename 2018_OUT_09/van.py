class Passageiro:
    def __init__(self, nome):
        self.nome = nome

class Van:
    lista = []
    def __init__(self, motorista=None):
        self.motorista = motorista

    def embarcar(self, Passageiro):
        self.lista.append(Passageiro)
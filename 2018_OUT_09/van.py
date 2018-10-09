class Passageiro:
    def __init__(self, nome):
        self.nome = nome

class Van:
    lista = []
    def __init__(self, motorista=None):
        self.motorista = motorista

    def embarcar(self, Passageiro):
        self.lista.append(Passageiro)

topic = Van('Orlando')
topic.embarcar(Passageiro('Passageiro 1'))
topic.embarcar(Passageiro('Passageiro 2'))
topic.embarcar(Passageiro('Passageiro 3'))
topic.embarcar(Passageiro('Passageiro 4'))
topic.embarcar(Passageiro('Passageiro 5'))
topic.embarcar(Passageiro('Passageiro 6'))
topic.embarcar(Passageiro('Passageiro 7'))
class Passageiro:
    def __init__(self, nome):
        self.nome = nome

class Van:
    
    def __init__(self, motorista=None):
        self.motorista = motorista
        self.lista = []

    def embarcar(self, Passageiro):
        if len(self.lista) < 16:
            self.lista.append(Passageiro)
        else:
            print('Van Lotada')

    def listar_passageiros(self):
        for item in self.lista:
            print(item.nome)


topic = Van('Orlando')
topic.embarcar(Passageiro('Passageiro 1'))
topic.embarcar(Passageiro('Passageiro 2'))
topic.embarcar(Passageiro('Passageiro 3'))
topic.embarcar(Passageiro('Passageiro 4'))
topic.embarcar(Passageiro('Passageiro 5'))
topic.embarcar(Passageiro('Passageiro 6'))
topic.embarcar(Passageiro('Passageiro 7'))
topic.embarcar(Passageiro('Passageiro 8'))
topic.embarcar(Passageiro('Passageiro 9'))
topic.embarcar(Passageiro('Passageiro 10'))
topic.embarcar(Passageiro('Passageiro 11'))
topic.embarcar(Passageiro('Passageiro 12'))
topic.embarcar(Passageiro('Passageiro 13'))
topic.embarcar(Passageiro('Passageiro 14'))
topic.embarcar(Passageiro('Passageiro 15'))
topic.embarcar(Passageiro('Passageiro 16'))
topic.embarcar(Passageiro('Passageiro 17'))
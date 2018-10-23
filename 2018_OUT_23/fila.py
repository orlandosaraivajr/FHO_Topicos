class filaBanco():
    def __init__(self):
        self.fila_pessoa_fisica = []
        self.fila_pessoa_juridica = []

    def entrar_cliente_pf(self, cliente):
        self.fila_pessoa_fisica.append(cliente)

    def entrar_cliente_pj(self, cliente):
        self.fila_pessoa_juridica.append(cliente)

    def atender_cliente_pf(self):
        try:
            atendido = self.fila_pessoa_fisica[0]
            self.fila_pessoa_fisica.remove(self.fila_pessoa_fisica[0])
            return atendido.nome
        except IndexError as e:
            return "Não temos mais clientes PF"
        
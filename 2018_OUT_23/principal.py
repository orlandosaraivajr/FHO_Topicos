from pacote1.pessoa import PessoaFisica
from pacote1.pessoa import PessoaJuridica


class filaBanco():
	def __init__(self):
		self.fila_pessoa_fisica = []
		self.fila_pessoa_juridica = []

	def entrar_cliente_pf(self, cliente):
		self.fila_pessoa_fisica.append(cliente)

	def entrar_cliente_pj(self, cliente):
		self.fila_pessoa_juridica.append(cliente)

if __name__ == '__main__':
    joao = PessoaFisica('João','123.434.657.94')
    jose = PessoaFisica('José da Silva','123.434.657.94')
    xyz = PessoaJuridica('xyz','1234')
    abc = PessoaJuridica('ABC','321')

    fila = filaBanco()
    
    fila.entrar_cliente_pf(joao)
    fila.entrar_cliente_pf(jose)
    fila.entrar_cliente_pj(xyz)
    fila.entrar_cliente_pj(abc)

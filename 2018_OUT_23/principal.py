from pacote1.pessoa import PessoaFisica
from pacote1.pessoa import PessoaJuridica
from fila import filaBanco


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
    print('Atendendo PF')
    print(fila.atender_cliente_pf())
    print(fila.atender_cliente_pf())
    print(fila.atender_cliente_pf())

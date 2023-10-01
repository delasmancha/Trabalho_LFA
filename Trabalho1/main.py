from Trabalho1.Minimizacao import Minimizacao
from Trabalho1.AFD import AFD

if __name__ == '__main__':
    teste = AFD('ab')
    for i in range(1, 5):
        teste.criaEstado(i)

    teste.mudaEstadoInicial(1)
    teste.mudaEstadoFinal(4, True)

    teste.criaTransicao(1, 2, 'a')
    teste.criaTransicao(2, 1, 'a')
    teste.criaTransicao(3, 4, 'a')
    teste.criaTransicao(4, 3, 'a')
    teste.criaTransicao(1, 3, 'b')
    teste.criaTransicao(3, 1, 'b')
    teste.criaTransicao(2, 4, 'b')
    teste.criaTransicao(4, 5, 'b')

    teste.criaEstado(5)
    teste.criaTransicao(5, 1, 'a')
    teste.criaTransicao(5, 4, 'b')

    print(Minimizacao.stateEq(teste, 1, 5))
    print(Minimizacao.stateEq(teste, 2, 5))

    teste.criaEstado(6)
    teste.criaTransicao(6, 2, 'a')
    teste.criaTransicao(6, 2, 'b')
    teste.criaEstado(7)
    teste.criaTransicao(7, 5, 'a')
    teste.criaTransicao(7, 5, 'b')

    print(Minimizacao.stateEq(teste, 6, 7))

    teste.criaEstado(8)
    teste.criaTransicao(8, 6, 'a')
    teste.criaTransicao(8, 3, 'b')
    teste.criaEstado(9)
    teste.criaTransicao(9, 7, 'a')
    teste.criaTransicao(9, 1, 'b')

    print(Minimizacao.stateEq(teste, 8, 9))

    print(teste)

    Minimizacao.minimizacao(teste)
    print(teste)

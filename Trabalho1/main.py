import AFD_jflap as jflap
from Minimizacao import Minimizacao
from Multiplicacao import Multiplicacao
from Operacoes_Conjunto import Operacoes as op

from AFD import AFD

def copia():
    aux = int(input(("Digite o número AFD de origem: ")))
    copiado = AFD("ab")
    if aux == 1:
        copiado = AFD.copiaAFD(afd1, afd3)
    elif aux == 2:
         copiado =AFD.copiaAFD(afd2, afd3)
    elif aux == 3:
         copiado = AFD.copiaAFD(afd3, afd3)
    elif aux == 4:
         copiado = AFD.copiaAFD(afd4, afd3)
    return copiado 

def opcj(afd1, afd2):
    aux = 0
    afd_res = AFD('z')
    a1 = AFD('z')
    a1 = AFD.copiaAFD(afd1, a1)
    a2 = AFD('z')
    a2 = AFD.copiaAFD(afd1, a2)
    afd_res = Multiplicacao.multi(afd1, afd2)
    if aux != 6:
            print("1- Multiplicação")
            print("2- União")
            print("3- Instersecção")
            print("4- Diferença")
            print("5- Complemento")
            print("6- Sair")
            aux = int(input("Digite a Opção Desejada: "))
            if aux == 1:
                return afd_res
            if aux == 2:
                afd_res = op.uni(a1, a2, afd_res)
                return afd_res
            if aux == 3:
                afd_res = op.inter(a1, a2, afd_res)
                return afd_res
            if aux == 4:
                afd_res = op.dif(a1, a2, afd_res)
                return afd_res
            if aux == 5:
                afd_res = op.comp(a1)
                return afd_res
    return afd_res

if __name__ == "__main__":
    teste = AFD("ab")
    for i in range(1, 5):
        teste.criaEstado(i)
        # if i == 1:
        #     teste.criaEstado(i, True)
        # if i == 4:
        #     teste.criaEstado(i, False, True)
        # else:
        #     teste.criaEstado(i)

    teste.mudaEstadoInicial(1)
    teste.mudaEstadoFinal(4, True)
    teste.mudaEstadoFinal(1, True)

    teste.criaTransicao(1, 2, "a")
    teste.criaTransicao(2, 1, "a")
    teste.criaTransicao(3, 4, "a")
    teste.criaTransicao(4, 3, "a")
    teste.criaTransicao(1, 3, "b")
    teste.criaTransicao(3, 1, "b")
    teste.criaTransicao(2, 4, "b")
    teste.criaTransicao(4, 2, "b")

    teste.criaEstado(5)
    teste.criaTransicao(5, 1, "a")
    teste.criaTransicao(5, 4, "b")

    # print(Minimizacao.stateEq(teste, 1, 5))
    # print(Minimizacao.stateEq(teste, 2, 5))

    teste.criaEstado(6)
    teste.criaTransicao(6, 2, "a")
    teste.criaTransicao(6, 2, "b")
    teste.criaEstado(7)
    teste.criaTransicao(7, 5, "a")
    teste.criaTransicao(7, 5, "b")

    # print(Minimizacao.stateEq(teste, 6, 7))

    teste.criaEstado(8)
    teste.criaTransicao(8, 6, "a")
    teste.criaTransicao(8, 3, "b")
    teste.criaEstado(9)
    teste.criaTransicao(9, 7, "a")
    teste.criaTransicao(9, 1, "b")

    # print(teste.alfabeto)
    # print(Minimizacao.stateEq(teste, 8, 9))
    # print(teste.estados)
    # print(teste.transicoes)
    # print(type  (teste.transicoes.items()))
    # for cs in teste.transicoes.items():
    # print(cs[0])
    # print(teste.finais)
    """ multi = Multiplicacao.multi(teste, teste)
    #print(multi)
    op1 = multi.copiaAFD(multi, multi)
    op2 = multi.copiaAFD(multi, multi)
    op3 = multi.copiaAFD(multi, multi)
    print(op3)
    intersecao = op.inter(teste, teste, multi)
    print(op3)
    uniao = op.uni(teste, teste, multi)
    print(op3)
    teste1 = teste.copiaAFD(teste, teste)
    diferenca = op.dif(teste1, teste, multi) 
    complemento = op.comp(teste)
    print(complemento)"""

    opc = 99999
    afd_copia = AFD("ab")
    afd1 = AFD("ab")
    afd2 = AFD("ab")
    afd3 = AFD.copiaAFD(teste, afd_copia)
    afd4 = AFD("abs")
    count = 1


    Minimizacao.minimizacao(teste)
    print(teste)



    # # Teste Equivalência de Autômatos
    af1 = AFD('ab')
    for i in range(0, 4):
        af1.criaEstado(i)
    af1.mudaEstadoInicial(0)
    af1.mudaEstadoFinal(2, True)
    af1.criaTransicao(0, 1, 'a')
    af1.criaTransicao(0, 0, 'b')
    af1.criaTransicao(1, 2, 'a')
    af1.criaTransicao(1, 0, 'b')
    af1.criaTransicao(2, 2, 'a')
    af1.criaTransicao(2, 2, 'b')
    af1.criaTransicao(3, 3, 'a')
    af1.criaTransicao(3, 3, 'b')

    af2 = AFD('ab')
    for i in range(1, 5):
        af2.criaEstado(i)
    af2.mudaEstadoInicial(1)
    af2.mudaEstadoFinal(3, True)
    af2.criaTransicao(1, 1, 'a')
    af2.criaTransicao(1, 0, 'b')
    af2.criaTransicao(2, 2, 'a')
    af2.criaTransicao(2, 4, 'b')
    af2.criaTransicao(3, 3, 'a')
    af2.criaTransicao(3, 3, 'b')
    af2.criaTransicao(4, 4, 'a')
    af2.criaTransicao(4, 4, 'b')

    print(Minimizacao.afEq(af1, af2))

    af3 = AFD('ab')
    for i in range(0, 4):
        af1.criaEstado(i)
    af1.mudaEstadoInicial(0)
    af1.mudaEstadoFinal(2, True)
    af1.criaTransicao(0, 1, 'a')
    af1.criaTransicao(0, 0, 'b')
    af1.criaTransicao(1, 2, 'a')
    af1.criaTransicao(1, 0, 'b')
    af1.criaTransicao(2, 2, 'a')
    af1.criaTransicao(2, 2, 'b')
    af1.criaTransicao(3, 3, 'a')
    af1.criaTransicao(3, 3, 'b')

    af4 = AFD('ab')
    for i in range(1, 5):
        af2.criaEstado(i)
    af2.mudaEstadoInicial(1)
    af2.mudaEstadoFinal(4, True)
    af2.criaTransicao(1, 1, 'a')
    af2.criaTransicao(1, 0, 'b')
    af2.criaTransicao(2, 2, 'a')
    af2.criaTransicao(2, 2, 'b')
    af2.criaTransicao(3, 3, 'a')
    af2.criaTransicao(3, 3, 'b')
    af2.criaTransicao(4, 4, 'a')
    af2.criaTransicao(4, 4, 'b')

    print(Minimizacao.afEq(af1, af2))
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

    print("Bem Vindo!\n")
    print("Leia as opções do menu e deposi escolha uma das opções abaixo!")
    while opc != 6:
        print("1- Leitura e Escrita de AFDs")
        print("2- Copia de AFDs")
        print("3- Equivalência de AFDs")
        print("4- Operações de Conjunto")
        print("5- printar todos os AFDs")
        print("6- Sair")
        opc = int(input("Digite a Opção Desejada: "))
        if opc == 1:
            opc1 = 99999
            caminho = ""
            if opc1 != 5:
                print("1- Leitura de um arquivo de texto")
                print("2- Escrita em um arquivo de texto")
                print("3- Leitura pelo JFLAP")
                print("4- Escrita pelo JFLAP")
                print("5- Sair")
                opc1 = int(input("Digite a Opção Desejada: "))
                if opc1 == 1:
                    caminho = input("Digite o caminho de onde deseje ler o AFD: ")
                    if(count == 1):
                        afd1 = AFD.loadAF(caminho)
                        print(afd1)
                        count = 2
                    else:
                        afd2 = AFD.loadAF(caminho)
                        print(afd2)
                        count = 1    
                elif opc1 == 2:
                    caminho = input("Digite o caminho de onde deseje salvar o AFD: ")
                    count = int(input("Digite o número do AFD que deseja Salvar: "))
                    if count == 1:
                        AFD.saveAf(afd1, caminho)
                    elif count == 2:
                        AFD.saveAf(afd2, caminho)
                    elif count == 3:
                        AFD.saveAf(afd3, caminho)
                    elif count == 4:
                        AFD.saveAf(afd4, caminho)
                    count = 1
                elif opc1 == 3:
                    if(count == 1):
                        afd1 = jflap.lerAFD()
                        print(afd1)
                        count = 2
                    else:
                        afd2 = jflap.lerAFD()
                        print(afd2)
                        count = 1
                elif opc1 == 4:
                    count = int(input("Digite o número do AFD que deseja Salvar: "))
                    if count == 1:
                        jflap.escreveAFD(afd1)
                    elif count == 2:
                        jflap.escreveAFD(afd2)
                    elif count == 3:
                        jflap.escreveAFD(afd3)
                    elif count == 4:
                        jflap.escreveAFD(afd4)
                    count = 1
        elif opc == 2:
            afd3 = copia()
            print(afd3)
        elif opc == 3:
            opc1 = 99999
            if opc1 != 4:
                print("1- Equivalência de estados em um AFD")
                print("2- Equivalência de AFDs")
                print("3- Minimização de um AFD")
                print("4- Sair")
                opc1 = int(input("Digite a Opção Desejada: "))
                if opc1 == 1:
                    print("zaaaaaaaa")
                elif opc1 == 2:
                    boolean = Minimizacao.afEq(afd1, afd2)
                    if boolean == True:
                        print("\nAutômatos são equivalentes")
                    else:
                        print("\nAutômatos não são equivalentes")
                elif opc1 == 3:
                    afd4 = Minimizacao.minimizacao(afd1)
                    print(afd4)
        elif opc == 4:
            afd4 = opcj(afd1, afd2)
            print(afd4)
        elif opc == 5:
            print("                     AFD 1                   ")
            print(afd1)
            print("                     AFD 2                   ")
            print(afd2)
            print("                     AFD 3                   ")
            print(afd3)
            print("                     AFD 4                   ")
            print(afd4)
    # print(teste.transicoes.get((1, 'a')))

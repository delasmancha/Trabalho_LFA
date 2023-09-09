from Trabalho1.AFD import AFD

if __name__ == '__main__':
    teste = AFD('ab')
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

    teste.criaTransicao(1, 2, 'a')
    teste.criaTransicao(2, 1, 'a')
    teste.criaTransicao(3, 4, 'a')
    teste.criaTransicao(4, 3, 'a')
    teste.criaTransicao(1, 3, 'b')
    teste.criaTransicao(3, 1, 'b')
    teste.criaTransicao(2, 4, 'b')
    teste.criaTransicao(4, 2, 'b')
    teste.saveAf(teste, "teste.txt")
    af = teste.loadAF("teste.txt")

    print("AF :")
    print(af)


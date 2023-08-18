
def moveAFD(p, afd):
    atual = afd[0]
    final = afd[1]
    es = afd[2]
    for i in range(len(p)):
        for j in range(len(es)):
            if(atual == es[j][0] and p[i] == es[j][1]):
                atual = es[j][2]
                break
    if atual in final:
        print("Palavra Pertence a linguagem")
        return
    print("Palavra não Pertence a linguagem") 
    return

def AFD_exemplo():
    ini = 1;
    final = [2, 4]
    lista_es = [[1,'a',3], [1,'b',2], [2,'a',4], [2,'b',5],
    [3,'a',3], [3,'b',3], [4,'a',4], [4,'b',5], [5,'a',5], [5,'b',5]]
    palavra = input("Digite a String: ")
    afd = []
    afd.append(ini)
    afd.append(final)
    afd.append(lista_es)

    moveAFD(palavra, afd)
    return

def AFD_input():
    ini = int(input("Digite o estado inicial: "))
    finais = input("Digite os estados finais: ")
    finais = finais.split(",")#Separando o input do usuário
    finais = [int(numero) for numero in finais]#Convertendo os inputs para int
    afd = []

    opc = ""
    print("Hora de entrar com os estados e movimentos caso deseje sair apenas digite (sair)")
    print("Exemplo do que deve digitar: 1, a, 2")
    print("1 seria o estado de Origem")
    print("a seria o caractere da ligação")
    print("2 seria o estado-destino")

    lista_es = []

    while(True):
        aux = input("Digite: ")
        if(aux == "sair"):
            break
        aux = aux.split(",")
        aux[0] = int(aux[0])
        aux[2] = int(aux[2])
        lista_es.append(aux)

    afd.append(ini)
    afd.append(finais)
    afd.append(lista_es)
    palavra = input("Digite a String: ")
    moveAFD(palavra, afd)
    while(True):
        print("\n")
        palavra = input("Digite a String: ")
        if(palavra == "sair"):
            return
        moveAFD(palavra, afd)

def lerAFD():
    return
def escreverAFD():
    return
    


#AFD_exemplo()
AFD_input()
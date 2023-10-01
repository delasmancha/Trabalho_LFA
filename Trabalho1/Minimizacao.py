class Minimizacao:
    def __init__(self):
        from Trabalho1.AFD import AFD

    @staticmethod
    def stateEq(afd, id1, id2):
        # Casos Triviais: 1- Se um dos dois estados não estiver no afd.
        if id1 not in afd.estados or id2 not in afd.estados:
            return False
        # 2- Se um dos estados for inicial.
        elif (id1 == afd.inicial or id2 == afd.inicial) and (id1 != id2):
            return False
        # 3- Se um dos estados for final, e o outro não.
        elif (id1 in afd.finais and id2 not in afd.finais) or (id2 in afd.finais and id1 not in afd.finais):
            return False
        # 4- Se ambos estados sâo iguais.
        elif id1 == id2:
            return True
        # Verificação de transições: itera o alfabeto
        controle = 0
        for i in afd.alfabeto:
            # Se um dos estados tiver transição com aquele caractere do alfabeto e o outro não,
            # os estados são diferentes.
            if (afd.transicoes.get((id1, i)) is None and afd.transicoes.get((id2, i)) is not None) or (
                    afd.transicoes.get((id1, i)) is not None and afd.transicoes.get((id2, i)) is None):
                return False
            # Se as transições forem iguais e o algoritmo já testou todo o alfabeto.
            if afd.transicoes.get((id1, i)) == afd.transicoes.get((id2, i)) and i == afd.alfabeto[
                len(afd.alfabeto) - 1]:
                return True
            # Caso contrário, testa as transições seguintes, até terminar o alfabeto inteiro.
            elif afd.transicoes.get((id1, i)) is not None or afd.transicoes.get((id2, i)) is not None:
                if Minimizacao.stateEq(afd, afd.transicoes.get((id1, i)), afd.transicoes.get((id2, i))):
                    pass
                else:
                    return False
        # Se o algoritmo não verificou nenhuma diferença entre os estados, então eles são iguais.
        return True

    @staticmethod
    def afEq(afd1, afd2):
        if Minimizacao.stateEq(afd1.inicial, afd2.inicial):
            return True
        return False

    @staticmethod
    def minimizacao(afd):
        equivalentes = []
        for i in afd.estados:
            aux = []
            for j in afd.estados:
                if [i, j] in equivalentes or [j, i] in equivalentes:
                    continue
                if Minimizacao.stateEq(afd, i, j) and i != j:
                    aux.append(i)
                    aux.append(j)
                if not aux or aux in equivalentes:
                    continue
                equivalentes.append(aux)
        for i in equivalentes:
            for j in afd.estados:
                for k in afd.alfabeto:
                    if (j, k) in afd.transicoes:
                        if afd.transicoes[(j, k)] == i[1] and j != i[1]:
                            del afd.transicoes[(j, k)]
                            afd.criaTransicao(j, i[0], k)
                        if j == i[1]:
                            del afd.transicoes[(j, k)]
            afd.estados.remove(i[1])
        return equivalentes

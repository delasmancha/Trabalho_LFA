class Minimizacao:
    def __init__(self):
        from Trabalho1.AFD import AFD

    @staticmethod
    def __transicoes(afd):
        transicoes = []
        for i in afd.estados:
            for j in afd.alfabeto:
                if (i, j) in afd.transicoes.keys():
                    transicoes.append([i, afd.transicoes.get((i, j)), j])
        return transicoes

    @staticmethod
    def stateEq(afd, id1, id2, visited=None):
        # Se os estados são iguais, são equivalentes.
        if id1 == id2:
            return True

        # Inicialização de estados visitados.
        if visited is None:
            visited = set()

        # Se os estados já foram visitados, são equivalentes.
        if (id1, id2) in visited or (id2, id1) in visited:
            return True

        # Marca os estados como visitados.
        visited.add((id1, id2))

        # Verifica a equivalência para cada símbolo do alfabeto.
        for symbol in afd.alfabeto:
            next_state1 = afd.transicoes.get((id1, symbol))
            next_state2 = afd.transicoes.get((id2, symbol))

            # Se uma transição é nula e a outra não, os estados não são equivalentes.
            if (next_state1 is None) != (next_state2 is None):
                return False

            # Se ambas as transições não são nulas, verifica a equivalência recursivamente.
            if next_state1 is not None and next_state2 is not None:
                if not Minimizacao.stateEq(afd, next_state1, next_state2, visited):
                    return False

        # Se não foi encontrado motivo para serem diferentes, os estados são equivalentes.
        return True

    @staticmethod
    def estadosEquivalentes(afd):
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
        return equivalentes

    @staticmethod
    def concatAF(afd1, afd2):
        for i in afd2.estados:
            afd1.criaEstado(int("1{}".format(i)))
            for j in afd1.alfabeto:
                if (i, j) in afd2.transicoes:
                    afd1.criaTransicao(int("1{}".format(i)), "1{}".format(afd2.transicoes.get((i, j))), j)
            if i in afd2.finais:
                afd1.mudaEstadoFinal("1{}".format(i), True)
        return afd1

    @staticmethod
    def afEq(afd1, afd2):
        afConcatenado = Minimizacao.concatAF(afd1, afd2)
        if Minimizacao.stateEq(afConcatenado, afd1.inicial, afd2.inicial):
            return True
        else:
            return False

    @staticmethod
    def minimizacao(afd):
        equivalentes = Minimizacao.estadosEquivalentes(afd)
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

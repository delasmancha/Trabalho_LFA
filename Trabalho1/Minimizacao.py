class Minimizacao:
    def __init__(self):
        from Trabalho1.AFD import AFD

    @staticmethod
    def stateEq(afd, id1, id2):
        # Casos Triviais: 1- Se um dos dois estados não estiver no afd.
        if id1 not in afd.estados or id2 not in afd.estados:
            return False
        # 2- Se um dos estados for inicial.
        elif id1 == afd.inicial or id2 == afd.inicial:
            return False
        # 3- Se um dos estados for final, e o outro não.
        elif (id1 in afd.finais and id2 not in afd.finais) or (id2 in afd.finais and id1 not in afd.finais):
            return False
        # Verificação de transições: itera o alfabeto
        controle = 0
        for i in afd.alfabeto:
            if (afd.transicoes.get((id1, i)) is None and afd.transicoes.get((id2, i)) is not None) or (afd.transicoes.get((id1, i)) is not None and afd.transicoes.get((id2, i)) is None):
                return False
            if afd.transicoes.get((id1, i)) == afd.transicoes.get((id2, i)) and i == afd.alfabeto[len(afd.alfabeto)-1]:
                return True
            elif afd.transicoes.get((id1, i)) is not None or afd.transicoes.get((id2, i)) is not None:
                if Minimizacao.stateEq(afd, afd.transicoes.get((id1, i)), afd.transicoes.get((id2, i))):
                    controle = 1
        if controle == 1:
            return True
        return False

    def afEq(self, afd1, afd2):
        pass

    def minimizacao(self, afd):
        pass

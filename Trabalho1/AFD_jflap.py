#from AFD import *
import xml.etree.ElementTree as ET

def lerAFD():
    local = input("Digite o local do arquivo a ser lido: ")
    # Ler o conteúdo do arquivo
    with open('JFLAP/teste1.jff', 'r') as p:
        xml_content = p.read()

    # Analisa o conteúdo XML
    root = ET.fromstring(xml_content)
    # Inicializa as variáveis
    id_inicial = None
    ids_finais = []
    lista_es = []
    origem = []
    car = []
    destino = []
    afd = []
    aux2 = [0, '*', 0]

    #Pegando os estados
    for estado in root.findall('.//state'):
        state_id = estado.get('id')
        for child in estado:
            if child.tag == 'initial':#Verifica se o estado tem a tag initial, se tiver pega o id do estado
                id_inicial = int(state_id)+1
            elif child.tag == 'final':
                ids_finais.append(int(state_id)+1)

    for transicao in root.findall('.//transition'):
        for aux1 in transicao.findall('./from'):
            k = aux1.text
            origem.append(int(k)+1)
        for aux1 in transicao.findall('./read'):
            r = aux1.text
            car.append(r)
        for aux1 in transicao.findall('./to'):
            s = aux1.text
            destino.append(int(s)+1)
        
    for i in range(len(car)):
        aux2[0] = origem[i]
        aux2[1] = car[i]
        aux2[2] = destino[i]
        aux3 = []
        aux3=aux3 + aux2
        lista_es.append(aux3)


    # Imprime os resultados
    afd.append(id_inicial)
    afd.append(ids_finais)
    afd.append(lista_es)

    return afd

afd = lerAFD()
    
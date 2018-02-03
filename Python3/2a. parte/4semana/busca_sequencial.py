"""Implemente a função busca(sequenz, elemento), que busca um determinado elemento em uma sequenz
e devolve o índice correspondente à posição do elemento encontrado. Utilize o algoritmo de
busca sequencial. Nos casos em que o elemento buscado não existir na sequenz, a função deve
devolver o booleano False. """

def busca(sequenz,element):
    for i in range(len(sequenz)):
        if sequenz[i] == element:
            return i
    return False
    


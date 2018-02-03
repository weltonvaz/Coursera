"""Escreva a função ordenada(lista), que recebe uma lista com números inteiros como parâmetro
e devolve o booleano True se a lista estiver ordenada e False se a lista não estiver ordenada."""

def ordenada(lista):
    Ende = len(lista)
    for i in range (Ende - 1):
        untere_pos = i
        for j in range (i + 1, Ende):
            if lista[j] < lista[untere_pos]:
                return False
    return True
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e devolve um
    número inteiro correspondente ao maior valor presente na lista recebida.
"""

def remove_repetidos(lista):
    return sorted(list(set(lista)))

def maior_elemento(maior):
    listamaior = remove_repetidos(maior)
    return max(listamaior)


numbers = []

while True:
    n = int(input("Digite um numero, 0 para SAIR: "))
    if n != 0:
        numbers.append(n)
    else:
        break
print(maior_elemento(numbers))
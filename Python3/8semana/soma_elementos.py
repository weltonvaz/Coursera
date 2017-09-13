#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número
    inteiro correspondente à soma dos elementos da lista recebida.
"""
def soma_elementos(lista):
    return sum(lista)

numbers = []

while True:
    n = int(input("Digite um numero, 0 para SAIR: "))
    if n != 0:
        numbers.append(n)
    else:
        break
print(soma_elementos(numbers))
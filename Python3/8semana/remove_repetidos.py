#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista
    possui elementos repetidos e os remove.
    A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve
    estar ordenada.
"""

def remove_repetidos(lista):
    return sorted(list(set(lista)))

numbers = []

while True:
    n = int(input("Digite um numero, 0 para SAIR: "))
    if n != 0:
        numbers.append(n)
    else:
        break
print(remove_repetidos(numbers))
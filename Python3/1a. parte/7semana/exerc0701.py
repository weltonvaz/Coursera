#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Escreva um programa que recebe como entradas (utilize a função input)
   dois números inteiros correspondentes à largura e à altura de um retângulo,
   respectivamente. O programa deve imprimir uma cadeia de caracteres que
   represente o retângulo informado com caracteres '#' na saída
"""

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

while altura >= 1:
    print("#"*largura)
    altura -= 1
    
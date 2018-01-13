#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreva um programa que receba um número natural n na entrada e
   imprima n! (fatorial) na saída. USANDO WHILE"""

n = int(input("Digite o valor INTEIRO: "))
while n >= 0:
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)
    n = int(input("Digite o valor INTEIRO: "))

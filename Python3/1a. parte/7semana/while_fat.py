#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreva um programa que receba um número natural n na entrada e imprima n! n! (fatorial) na saída."""

def fatorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        count = 1
        aux = 1
        while aux <= number:
            count = count * aux
            aux += 1
        return count


while True:
    number = int(input("Digite o valor de n: "))
    if number >= 0:
        print(fatorial(number))
    else:
        break

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Escreva um programa que receba um número natural n na entrada e imprima n! n! (fatorial) na saída."""

def fatorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        count = 1
        for fat in range(1,(number + 1)):
            count = count * fat
        return count

number = int(input("Digite o valor de n: "))

print(fatorial(number))
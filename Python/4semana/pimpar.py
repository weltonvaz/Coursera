#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Receba um número inteiro positivo na entrada e imprima os n n primeiros números ímpares naturais."""

number = int(input("Digite o valor de n: "))
count = 1
aux = 1

while aux <= number:
    print(count)
    count += 2
    aux = aux + 1
        
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fatores Primos"""

n = int(input("Digite o valor INTEIRO >1: "))


fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
       multiplicidade = multiplicidade + 1
       n = n / fator
       if multiplicidade > 0:
           print("Fator", fator, "Multiplicidade", multiplicidade)
    fator = fator + 1
    multiplicidade = 0

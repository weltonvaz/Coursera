#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" O coeficiente binomial, também chamado de número binomial, de um número n, na classe k, consiste no número de
    combinações de n termos, k a k. O número binomial de um número n, na classe k, pode ser escrito como:"""


def fatorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        count = 1
        for fat in range(1, (number + 1)):
            count = count * fat
        return count


def coefbinomial(n, k):
    return int(fatorial(n) / (fatorial(k) * fatorial(n - k)))


print("------------------------------")
print("Calcule o coeficiente binomial")

n = int(input("digite o valor para n: "))
k = int(input("digite o valor para k: "))

print(coefbinomial(n,k))
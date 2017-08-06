'''Faça um programa em Python que receba (entrada de dados) o valor correspondente
ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.'''

x = int(input("Digite o valor correspondente ao lado de um quadrado: "))

calArea = x ** 2
calPeri = x * 4

print("perímetro: %d - área: %d" %(calPeri,calArea))
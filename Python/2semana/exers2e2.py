'''Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja,
faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em
dias, horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, c minutos
e d segundos. Seja cuidadoso com o formato! Espaços a mais, vírgulas faltando ou outras
diferenças são considerados erro'''

x = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dia = divmod(x,86400)
hora = divmod(dia[1],3600)
minuto = divmod(hora[1],60)
segundo = minuto[1]

print("%d dias, %d horas, %d minutos e %d segundos." %(dia[0],hora[0],minuto[0],minuto[1]))
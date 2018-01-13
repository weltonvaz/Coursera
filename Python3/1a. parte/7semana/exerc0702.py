largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
rect = ''
while altura >= 1:
    for l in range(largura):
        if(l == 0 or altura == 0 or l == largura-1):
            rect += '#'
            continue
        rect += ' '
    rect += '\n'
    altura -= 1
print(rect)
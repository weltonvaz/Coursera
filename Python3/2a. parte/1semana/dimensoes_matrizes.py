def dimensoes(matriz):
    linhas = len(matriz)
    if linhas >= 0:
        colunas = len(matriz[0])
    else:
        linhas = 0
        colunas = 0

    print(str(linhas) + 'X' + str(colunas))

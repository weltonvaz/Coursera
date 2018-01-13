def dimensoes(m1,m2):
    cond = []
    for x in range(len(m1)):
        if len(m1[x]) == len(m2[x]):
            cond.append('True')
        else:
            cond.append('False')
    return cond

def matrix_soma(m1,m2):
    matriz_soma = []
    # Supondo que as duas matrizes possuem o mesmo tamanho
    quant_linhas = len(m1)
    quant_colunas = len(m1[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_soma
        matriz_soma.append([])
        for j in range(quant_colunas):
            # Somando os elementos que possuem o mesmo índice
            soma = m1[i][j] + m2[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma

def soma_matrizes(m1, m2):
    if dimensoes(m1,m2).count('False') == True:
        print('soma_matrizes(m1, m2) => False')
    else:
    # => [[3, 5, 7], [9, 11, 13]]
        print(matrix_soma(m1, m2))

m1 = [[1], [2], [3]]
m2 = [[2], [4], [5]]

soma_matrizes(m1, m2)
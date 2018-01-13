def somar(m1, m2):
    matriz_soma = []
    # Supondo que as duas matrizes possuem o mesmo tamanho
    quant_linhas = len(m1) # Conta quantas linhas existem
    quant_colunas = len(m1[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_soma
        matriz_soma.append([])
        for j in range(quant_colunas):
            # Somando os elementos que possuem o mesmo índice
            soma = m1[i][j] + m2[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma

def dimensoes(m1,m2):
    cond = []
    if len(m1) == len(m2):
        return soma_matrizes(m1,m2)
    
def soma_matrizes(m1,m2):
    if dimensoes(m1) != dimensoes(m2):
        return 'False'
    else:
        return somar(m1, m2)
        


m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

print(soma_matrizes(m1, m2))
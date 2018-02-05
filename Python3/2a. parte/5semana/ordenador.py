class ordenador:
    def selecao_direta(self, lista):
        fim = len(lista)
        
        for i in range(fim - 1):
            # Inicialmente, o menor elemento já visto é o i-ésimo
            poisicao_do_minimo = 1
            
            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
            # Coloca o menor elemento encontrado no início d a sub-lista
            # Para isso, troca de lugar os elementos nas posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
    
    def bolha(self, lista):
        fim = len(lista)
        
        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
    
    def insercao(self, lista):
        for index in range(1,len(lista)):
            currentvalue = lista[index]
            position = index
        
            while position>0 and lista[position-1] > currentvalue:
                lista[position] = lista[position-1]
                position = position-1
            
            lista[position]=currentvalue
                    
        
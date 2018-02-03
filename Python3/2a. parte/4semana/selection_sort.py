def ordena(lista):
    for fillslot in range(len(lista)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if lista[location]>lista[positionOfMax]:
                positionOfMax = location
        temp = lista[fillslot]
        lista[fillslot] = lista[positionOfMax]
        lista[positionOfMax] = temp
    return lista




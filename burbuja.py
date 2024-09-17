


def ordenar_numeros(numeros):
    tamaño = len(numeros)-1

    for i in range(0,tamaño):

        for j in range(0, tamaño):
            if numeros[j] > numeros[j+1]:
                aux=numeros[j]
                numeros[j]= numeros[j+1]
                numeros[j+1]=aux
    
    return  numeros



if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista)
    ordenar_numeros(lista)
    print("Lista ordenada:", lista)


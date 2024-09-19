


def ordenar_numeros(numeros):
    tamaño = len(numeros)-1

    for i in range(0,tamaño):

        for j in range(0, tamaño):
            if numeros[j] > numeros[j+1]:
                aux=numeros[j]
                numeros[j]= numeros[j+1]
                numeros[j+1]=aux
    
    return  numeros


def calcular_moda(lista):
    if len(lista) == 0:
        return "La lista está vacía. No se puede calcular la moda."
    
    conteo = {}
    
    # Contar las ocurrencias de cada número
    for i in lista:
        if i in conteo:
            conteo[i] += 1
        else:
            conteo[i] = 1
    
    # Encontrar el número con más ocurrencias
    moda = max(conteo, key=conteo.get)
    frecuencia = conteo[moda]
    print('diccionario',conteo)
    
    return moda, frecuencia

# Lista de ejemplo
lista = [64, 34, 25, 12, 22, 11, 90, 12, 12, 11]

# Llamar a la función y obtener la moda y su frecuencia
moda, frecuencia = calcular_moda(lista)
print("Moda:", moda)
print("Frecuencia:", frecuencia)



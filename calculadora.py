def calcular_media(numeros):
    if len(numeros) == 0:
        return "La lista está vacía. No se puede calcular la media."
    suma = sum(numeros)
    cantidad = len(numeros)
    media = suma / cantidad
    return f"La media de los siguientes números: {numeros} es: {media}"


def ordenar_numeros(numeros_mediana):
    tamaño = len(numeros_mediana) - 1

    for i in range(tamaño):
        for j in range(tamaño - i):
            if numeros_mediana[j] > numeros_mediana[j + 1]:
                aux = numeros_mediana[j]
                numeros_mediana[j] = numeros_mediana[j + 1]
                numeros_mediana[j + 1] = aux    
    return numeros_mediana

    
def calcular_mediana(numeros_mediana):
    if len(numeros_mediana) == 0:
        return "La lista está vacía. No se puede calcular la mediana."
    
    numeros_ordenados = ordenar_numeros(numeros_mediana)
    n = len(numeros_ordenados)    

    if n % 2 == 1: 
        # En el caso de que el tamaño del arreglo sea impar entonces la mediana es el numero que se encuntra en la mitad de este.
        mediana = numeros_ordenados[n // 2]
    else: 
        # En el caso de que el tamaño del arreglo sea par entonces la mediana es la suma de los dos numeros que se encuentran en el medio del arreglo.
        medio1 = numeros_ordenados[n // 2 - 1]
        medio2 = numeros_ordenados[n // 2]
        mediana = (medio1 + medio2) / 2

    return f"La mediana de los siguientes números: {numeros_ordenados} es: {mediana}"
    

def calcular_moda(numeros):
    if len(numeros) == 0:
        return "La lista está vacía. No se puede calcular la moda."
    
     # Se crea un diccionario llamado "conteo" para almacenar la cantidad de veces que se repite un numero en el arreglo
    conteo = {}
    
    # Ciclo para recorrer el arreglo y determinar la cantidad de veces que se repite un numero
    for i in numeros:
        # Si encuentra el numero en el diccionario entonces aumenta en uno su cantidad
        if i in conteo:
            conteo[i] += 1
        # En el caso de que el numero no se encuentre solo se aumenta uno ya que seria la primera vez que lo encuentra
        else:
            conteo[i] = 1
    
    # Encontrar el número que mas se repite
    moda = max(conteo, key=conteo.get)
    frecuencia = conteo[moda]
    
    return f"La moda de los siguientes números: {numeros} es: {moda}, que aparece {frecuencia} veces."

    
def calcular_desviacion_estandar(base_mayor, base_menor, altura):
    try:
        base_mayor = float(base_mayor)
        base_menor = float(base_menor)
        altura = float(altura)
        
        if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
            return "La base mayor, la base menor y la altura deben ser mayores que cero."
        
        if base_menor > base_mayor:
            return "La base menor no puede ser mayor que la base mayor."

        return f"El área del trapecio es: {((base_mayor + base_menor) * altura) / 2}"
    
    except ValueError:
        return "Los datos ingresados no son numéricos."

    

    

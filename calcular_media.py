def calcular_media(numeros):
    if len(numeros) == 0:
        return "La lista está vacía. No se puede calcular la media."
    suma = sum(numeros)
    cantidad = len(numeros)
    media = suma / cantidad
    return f"La media de los siguientes números: {numeros} es: {media}"



    
    
def calcular_mediana(base,altura):
    try:
        base = float(base)
        altura = float(altura)
        
        if base <= 0 or altura <= 0:
            return "La base y la altura deben ser valores mayores que cero."
        
        return f"El área del rectangulo es: {(base * altura)}"
    
    except ValueError:
        return "Los datos ingresados no son numéricos."
    

def area_cuadrado(lado):
    try:
        lado=float(lado)

        if lado <= 0:
            return "El lado del cuadrado debe ser mayor que cero."
        
        return f"El area del cuadrado es: {lado**2}"
  
    except ValueError:
        return "El dato ingresado no es numerico"
    

    
def area_trapecio(base_mayor, base_menor, altura):
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

    

    
def area_rombo(diagonal_mayor, diagonal_menor):
    try:
        diagonal_mayor = float(diagonal_mayor)
        diagonal_menor = float(diagonal_menor)

        
        if diagonal_mayor <= 0 or diagonal_menor <= 0 :
            return "La diagonal mayor y la diagonal menor deben ser mayores que cero."
        
        if diagonal_menor > diagonal_mayor:
            return "La diagonal menor no puede ser mayor que la diagonal mayor."

        return f"El área del rombo es: {(diagonal_mayor * diagonal_menor) / 2}"
    
    except ValueError:
        return "Los datos ingresados no son numéricos."

    

    
def area_circulo(radio):
    try:
        radio=float(radio)

        if radio <= 0:
            return "El radio del circulo debe ser mayor que cero."
        
        return f"El area del circlo es: { math.pi * (radio ** 2)}"
  
    except ValueError:
        return "El dato ingresado no es numerico"
   
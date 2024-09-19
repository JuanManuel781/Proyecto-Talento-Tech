import colores_print
from calculadora import *

estado = True
numeros = []

while estado:
    print(f'{colores_print.AZUL}=============================================================={colores_print.RESET}')
    print(f'{colores_print.AZUL}============ Calculadora de Estadísticas Básicas ============={colores_print.RESET}')
    print(f'{colores_print.AZUL}=============================================================={colores_print.RESET}')
    print(f'{colores_print.AZUL}1. Media{colores_print.RESET}')
    print(f'{colores_print.AZUL}2. Mediana{colores_print.RESET}')
    print(f'{colores_print.AZUL}3. Moda{colores_print.RESET}')
    print(f'{colores_print.AZUL}4. Desviación estándar{colores_print.RESET}')
    print(f'{colores_print.AZUL}5. Salir{colores_print.RESET}')

    numeros = []  

    try:
        opcion = int(input('Ingrese qué opción quiere realizar: '))
        
        if opcion == 1:
            opcion_uno = int(input('Ingrese cuántos números quiere ingresar para calcular la media: '))
            for _ in range(opcion_uno):
                while True:
                    try:
                        elemento = int(input('Ingrese un número: '))
                        if elemento <= 0:
                            print(f'{colores_print.ROJO}El número ingresado debe ser mayor que 0.{colores_print.RESET}')
                        else:
                            numeros.append(elemento)
                            break
                    except ValueError:
                        print(f'{colores_print.ROJO}El parámetro ingresado no es válido. Debe ser un número entero.{colores_print.RESET}')

            resultado = calcular_media(numeros)
            print(f'{colores_print.VERDE}{resultado}{colores_print.RESET}')

        elif opcion == 2:
            opcion_dos = int(input('Ingrese cuántos números quiere ingresar para calcular la mediana: '))
            numeros = []  # Inicializa la lista de números
            for _ in range(opcion_dos):
                while True:
                    try:
                        elemento = int(input('Ingrese un número: '))
                        if elemento <= 0:
                            print(f'{colores_print.ROJO}El número ingresado debe ser mayor que 0.{colores_print.RESET}')
                        else:
                            numeros.append(elemento)
                            break
                    except ValueError:
                        print(f'{colores_print.ROJO}El parámetro ingresado no es válido. Debe ser un número entero.{colores_print.RESET}')
    
            print(f'{colores_print.VERDE}{calcular_mediana(numeros)}{colores_print.RESET}')

        elif opcion == 3:
            opcion_tres = int(input('Ingrese cuántos números quiere ingresar: '))
            for _ in range(opcion_tres):
                while True:
                    try:
                        elemento = int(input('Ingrese un número: '))
                        if elemento <= 0:
                            print(f'{colores_print.ROJO}El número ingresado debe ser mayor que 0.{colores_print.RESET}')
                        else:
                            numeros.append(elemento)
                            break
                    except ValueError:
                        print(f'{colores_print.ROJO}El parámetro ingresado no es válido. Debe ser un número entero.{colores_print.RESET}')
            print(f'{colores_print.VERDE}{calcular_moda(numeros)}{colores_print.RESET}')

        elif opcion == 4:
            opcion_cuatro = int(input('Ingrese cuántos números quiere ingresar: '))
            for _ in range(opcion_cuatro):
                while True:
                    try:
                        elemento = int(input('Ingrese un número: '))
                        if elemento <= 0:
                            print(f'{colores_print.ROJO}El número ingresado debe ser mayor que 0.{colores_print.RESET}')
                        else:
                            numeros.append(elemento)
                            break
                    except ValueError:
                        print(f'{colores_print.ROJO}El parámetro ingresado no es válido. Debe ser un número entero.{colores_print.RESET}')
            print(f'{colores_print.VERDE}Desviación estándar es: {calcular_desviacion_estandar(numeros)}{colores_print.RESET}')

        elif opcion == 5:
            print("Gracias por utilizar la Calculadora de Estadísticas Básicas.")
            estado = False
        else:
            print(f'{colores_print.ROJO}Opción no válida. Por favor, ingrese una opción del 1 al 5 para seleccionar una operación.{colores_print.RESET}')
    
    except ValueError:
        print(f'{colores_print.ROJO}====================================={colores_print.RESET}')
        print(f'{colores_print.ROJO}La opción ingresada no es válida. Debe ser un número entero.{colores_print.RESET}')
        print(f'{colores_print.ROJO}====================================={colores_print.RESET}')
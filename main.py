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
    print(f'{colores_print.AZUL}4. Varianza{colores_print.RESET}')
    print(f'{colores_print.AZUL}5. Desviación estándar{colores_print.RESET}')
    print(f'{colores_print.AZUL}6. Salir{colores_print.RESET}')

    numeros = []  

    try:
        opcion = int(input('Ingrese qué opción quiere realizar: '))
        
        if opcion == 1:
            opcion_uno = int(input('Ingrese la cantidad de numeros que requiera para calcular la media: '))
            if opcion_uno >0:
                for _ in range(opcion_uno):
                    while True:
                        try:
                            elemento = int(input('Ingrese un número: '))
                            numeros.append(elemento)  
                            break
                        except ValueError:
                            print(f'{colores_print.ROJO}El parámetro ingresado no es válido. Debe ser un número entero.{colores_print.RESET}')

                print(f'{colores_print.VERDE}La media de los siguientes numeros:{numeros} es: {calcular_media(numeros)}{colores_print.RESET}')
            else:
                print(f'{colores_print.ROJO}La opción ingresada no es válida. Debe ser un número entero mayor que 0.{colores_print.RESET}') 
        elif opcion == 2:
            opcion_dos = int(input('Ingrese la cantidad de numeros que requiera para calcular la mediana: '))
            if opcion_dos >0 :
                for _ in range(opcion_dos):
                    while True:
                        try:
                            elemento = int(input('Ingrese un número: '))
                            numeros.append(elemento)  
                            break
                        except ValueError:
                            print(f'{colores_print.ROJO}El parámetro ingresado no es válido. Debe ser un número entero.{colores_print.RESET}')
        
                print(f'{colores_print.VERDE}{calcular_mediana(numeros)}{colores_print.RESET}')
            else:
                print(f'{colores_print.ROJO}La opción ingresada no es válida. Debe ser un número entero mayor que 0.{colores_print.RESET}') 


        elif opcion == 3:
            opcion_tres = int(input('Ingrese la cantidad de numeros que requiera para calcular la moda: '))
            if opcion_tres>0:
                for _ in range(opcion_tres):
                    while True:
                        try:
                            elemento = int(input('Ingrese un número: '))
                            numeros.append(elemento)  
                            break
                        except ValueError:
                            print(f'{colores_print.ROJO}El parámetro ingresado no es válido. Debe ser un número entero.{colores_print.RESET}')

                print(f'{colores_print.VERDE}{calcular_moda(numeros)}{colores_print.RESET}')
            else:
                print(f'{colores_print.ROJO}La opción ingresada no es válida. Debe ser un número entero mayor que 0.{colores_print.RESET}') 


        elif opcion == 4:
            opcion_cuatro = int(input('Ingrese la cantidad de numeros que requiera para calcular la varianza: '))
            if opcion_cuatro >0:
                for _ in range(opcion_cuatro):
                    while True:
                        try:
                            elemento = int(input('Ingrese un número: '))
                            numeros.append(elemento)  
                            break
                        except ValueError:
                            print(f'{colores_print.ROJO}El parámetro ingresado no es válido. Debe ser un número entero.{colores_print.RESET}')

                varianza1, varianza2 = calcular_varianza(numeros)
                print(f'{colores_print.VERDE}La varianza teniendo en cuenta la POBLACION de los siguientes numeros {numeros} es: {varianza1:.2f} \nLa varianza teniendo en cuenta la MUESTRA de los siguientes numeros {numeros} es: {varianza2:.2f}{colores_print.RESET}')
            else:
                print(f'{colores_print.ROJO}La opción ingresada no es válida. Debe ser un número entero mayor que 0.{colores_print.RESET}') 

        elif opcion == 5:
            opcion_cinco = int(input('Ingrese la cantidad de numeros que requiera para calcular la desviación estandar: '))
            if opcion_cinco:
                for _ in range(opcion_cinco):
                    while True:
                        try:
                            elemento = int(input('Ingrese un número: '))
                            numeros.append(elemento)  
                            break
                        except ValueError:
                            print(f'{colores_print.ROJO}El parámetro ingresado no es válido. Debe ser un número entero.{colores_print.RESET}')
                    
                desviacion_estandar1, desviacion_estandar2 = calcular_varianza(numeros)
                print(f'{colores_print.VERDE}La desviación estandar teniendo en cuenta la POBLACION de los siguientes numeros {numeros} es: {desviacion_estandar1:.2f} \nLa desviación estandar teniendo en cuenta la MUESTRA de los siguientes numeros {numeros} es: {desviacion_estandar2:.2f}{colores_print.RESET}')
            else:
                print(f'{colores_print.ROJO}La opción ingresada no es válida. Debe ser un número entero mayor que 0.{colores_print.RESET}') 

        elif opcion == 6:
            print("Gracias por utilizar la Calculadora de Estadísticas Básicas.")
            estado = False
        else:
            print(f'{colores_print.ROJO}Opción no válida. Por favor, ingrese una opción del 1 al 5 para seleccionar una operación.{colores_print.RESET}')


    except ValueError:
        print(f'{colores_print.ROJO}====================================={colores_print.RESET}')
        print(f'{colores_print.ROJO}La opción ingresada no es válida. Debe ser un número entero.{colores_print.RESET}')
        print(f'{colores_print.ROJO}====================================={colores_print.RESET}')

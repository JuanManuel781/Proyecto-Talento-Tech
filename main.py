import colores_print

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

    try:
        opcion = int (input('Ingrese que opcion quiere realizar: '))
        
        if opcion ==1:
            opcion_uno = int (input('Ingrese cuantos numeros quiere ingresar: '))    
            for _ in range(opcion_uno):
                while True:
                    try:
                        elemento = int(input(f'Ingrese un numero: '))
                        if elemento <=0:
                            print(f'{colores_print.ROJO}El numero ingresado debe ser mayor que 0.{colores_print.RESET}')  
                        else:
                            numeros.append(elemento)
                            print(f'{colores_print.VERDE}Media es:{numeros}{colores_print.RESET}')
                            break
                    except (ValueError, TypeError):
            
                        print(f'{colores_print.ROJO}El parametro ingresada no es valido{colores_print.RESET}')      
        elif opcion ==2:
            opcion_dos = int (input('Ingrese cuanto numeros quiere ingresar: '))
            for _ in range(opcion_dos):
                while True: 
                    try:
                        elemento = int(input(f'Ingrese un numero: '))
                        if elemento <=0:
                             print(f'{colores_print.ROJO}El numero ingresado debe ser mayor que 0.{colores_print.RESET}')  
                        else:
                            numeros.append(elemento)
                            print(f'{colores_print.VERDE}Mediana es:{numeros}{colores_print.RESET}')
                            break
                    except (ValueError, TypeError):
                        print(f'{colores_print.ROJO}El parametro ingresada no es valido{colores_print.RESET}')     
        elif opcion ==3:
            opcion_tres = int (input('Ingrese cuanto numeros quiere ingresar: '))
            for _ in range(opcion_tres):
                while True: 
                    try:
                        elemento = int(input(f'Ingrese un numero: '))
                        if elemento <=0:
                            print(f'{colores_print.ROJO}El numero ingresado debe ser mayor que 0.{colores_print.RESET}')  
                        else:
                            numeros.append(elemento)
                            print(f'{colores_print.VERDE}Moda es:{numeros}{colores_print.RESET}')
                            break
                    except (ValueError, TypeError):
                        print(f'{colores_print.ROJO}El parametro ingresada no es valido{colores_print.RESET}')   
        elif opcion ==4:
            opcion_cuatro = int (input('Ingrese cuanto numeros quiere ingresar: '))
            for _ in range(opcion_cuatro):
                while True: 
                    try:
                        elemento = int(input(f'Ingrese un numero: '))
                        if elemento <=0:
                            print(f'{colores_print.ROJO}El numero ingresado debe ser mayor que 0.{colores_print.RESET}') 
                        else:
                            numeros.append(elemento)
                            print(f'{colores_print.VERDE}Desviación estándar es:{numeros}{colores_print.RESET}')
                            break
                    except (ValueError, TypeError):
                        print(f'{colores_print.ROJO}El parametro ingresada no es valido{colores_print.RESET}')   
            
        elif opcion == 5:
            print("Gracias por utilizar la Calculadora de Estadísticas Básicas.")
            estado = False
        else:
            print("Opción no válida. Por favor, ingrese una opcion del 1 al 4 para seleccionar una operación.")
    
    except (ValueError, TypeError):
        print(f'{colores_print.ROJO}====================================={colores_print.RESET}')
        print(f'{colores_print.ROJO}la opcion ingresada no existe{colores_print.RESET}')
        estado = True
        print(f'{colores_print.ROJO}====================================={colores_print.RESET}')


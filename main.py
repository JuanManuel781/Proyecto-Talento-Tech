estado = True

while estado:
    print('==============================================================')
    print('============ Calculadora de Estadísticas Básicas =============')
    print('==============================================================')
    print('1. Media')
    print('2. Mediana')
    print('3. Desviación estándar')
    print('4. Salir')

    try:
        opcion = int (input('Ingrese que opcion quiere realizar: '))
        
        

        if opcion ==1:
            print('Calcular Media')

        elif opcion ==2:
            print('Calcular Mediana')
        
        elif opcion ==3:
            print('Calcular Desviación estándar')

        elif opcion == 4:
            estado = False
        else:
            print("Opción no válida. Por favor, ingrese una opcion del 1 al 4 para seleccionar una operación.")
    
    except (ValueError, TypeError):
        print('=====================================')
        print('la opcion ingresada no existe')
        estado = True
        print('=====================================')


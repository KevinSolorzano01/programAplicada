"""Este código es un programa que verifica si un número ingresado por 
el usuario es primo o no, y permite continuar verificando números hasta que decida detenerse.""" 

a = 1
value = input('Ingrese un valor')
value = int(value)

while a == 1:
    for i in range(1,value+1):
        conta = 0
        for n in range(1, i+1):
            residue = i%n
            if residue == 0:
                conta = conta + 1
            
            # print("i = ", i)
            # print("n = ", n)
            # print("residue = ", residue)
            # print("conta = ", conta)

"""Después de completar el bucle interno, se verifica si conta es igual a 2. Si es igual a 2, significa que 
el número i tiene exactamente dos divisores (1 y sí mismo), lo que lo hace primo. 
En ese caso, se imprime que i es un número primo. Si conta no es igual a 2, se imprime que i no es un número primo."""


    if conta == 2:
       print(f'{i} es un primo')
       print("\n")
    else:
       print(f'{i} NOOO es un primo')
       print("\n")

"""Se le pregunta al usuario si desea continuar verificando números. Si el usuario ingresa 1, el programa 
continúa ejecutándose y se solicita ingresar otro valor. Si el usuario ingresa cualquier otro número diferente
de 1, el programa se detiene gracias a la condición if a != 1: break. """

    print('Do you want to continue?. Press 1 to do that')
    a = input()
    a = int(a)

    if a != 1:
        break

    value = input('Ingrese un valor')
    value = int(value)

"""Este código es un bucle infinito que le pide al usuario 
que introduzca un número positivo y luego calcula el factorial de ese número si es un entero positivo"""

while True:
    valor =(input("introducion un numero positivo: "))
    print("Valor: ", valor)
    a = isinstance(valor,int)
    print(a)
    if a== True and valor > 0:
        fact=1
        for i in range(1, valor+1):
            fact=fact*i
            print(f'the factorial de {valor} es: ', fact)
    else:
        print("por favor, ingresar un numero positivo")

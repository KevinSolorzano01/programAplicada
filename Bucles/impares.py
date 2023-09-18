""" Este codigo analiza que numeros son paraes e impares  en un rango de numeros"""

for i in range(1,21):
    """determina si es impar o par con el modulo
    dando un residuo de 0 si es par y de 1 si es impar """
    residuo=i%2
    # imprime si es par o es impar dependiendo del residuo obtenido
    if residuo == 0:
        print(f'{i} es par')
    else:
        print(str(i)+'es impar')


for i in range(0,6):
    result = i**3
    print(result)


""" muestra como una variable puede cambiar
en cuanto al tipo, pasa de float a int """

times = input("Enter a number of times: ")
times = float(times)
times = int(times)
print(type(times))
print(times)

if times == 0:
    print("Don't do anything")
else:
    for i in range(1,times+1):
        print("i = ", i)

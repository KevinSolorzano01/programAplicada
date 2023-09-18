#muestra los numeros primos que hay en una rango de numeros ,tambien el tiempo en que se tarda en hacer esto en valores de milisegundos """

import time
inicio= time.time()#toma el valor del tiempo en que inicia
time.sleep(1)
for i in range (0,3):
    conta=0
    for n in range(1,i+1):
        residuo=i%n
        if residuo == 0:
            conta= conta+1
    if conta==2: 
        print(f'{i} es un primo')
fin= time.time()#toma el timepo en el que finaliza
print("t = ",(fin-inicio)*1000) #impreme el tiempo que tarda en ejecutarse el programa, restando el final con el inicial

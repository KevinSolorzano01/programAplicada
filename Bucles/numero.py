import random # usa generadores de numeros aleatorios 
from matplotlib import pyplot as plt # es un grupo de funciones la cual hacen un funcionamiento parecido a Matlab

#se genera un numero random
# Add your code below:
numbers_a = range(1, 13)
numbers_b = [random.randint(1, 1000) for i in range(12)]
plt.plot(numbers_a, numbers_b)
plt.show()

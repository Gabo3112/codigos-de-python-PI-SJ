#tarea usar una lista que permita ingresar numeros enteros.(minimo permita ingresar 10 numeros)
#luego crear una funcion que los ordene de manera ascendete.
#por ultimo imprimir la lista ordenada.

import random
num=[]
for c in range(10):
    valor=int(input("ingrese un numero: "))
    num.append(valor)

print(num)
ordenados=sorted(num)
print(ordenados)


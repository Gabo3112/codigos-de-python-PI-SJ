#diccionario: permite almacenar datos con llave-valor ,  no usa indice
# ´´ ={}
#tuplas: usan indices , no permite cambios
#´´=()
#listas: usan indices , si permiten cambios
#´´=[]


alumno={"nombre":"Gabriel","carrera":"informatica","ciudad":"Piura"}
print(alumno["ciudad"])

abreviatura=("Sr.","Dr.","Ing.","Sra.")
print(abreviatura[1])

notas=[13,16,15]
notas[0]=17
print(notas[0])

#tarea usar una lista que permita ingresar numeros enteros.(minimo permita ingresar 10 numeros)
#luego crear una funcion que los ordene de manera ascendete.
#por ultimo imprimir la lista ordenada.
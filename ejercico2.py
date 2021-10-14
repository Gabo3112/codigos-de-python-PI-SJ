num1=int(input("ingrese un numero: "))
num2=int(input("ingrese un numero: "))
num3= int(input("ingrese un numero: "))

if( num1>num2 and num1>num3):
    print("el numero mayor es: ",num1)
else:
    if(num2>num1 and num2>num3):
        print("el numero mayor es: ",num2)
    else:
        print("el numero mayor es: ",num3)
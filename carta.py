#Menu de opciones

opcion=100


#ciclo/bucle/iteracion

print(" Menú a la carta")
print("*****************************************")
print("1 ---> Calcular la suma")
print("2 ---> Calcular la resta")
print("3 ---> Calcular la multiplicación")
print("4 ---> Calcular la división")
print("0 ---> Salir")
print("*****************************************")


while(opcion!=0):
    opcion=int(input("Digita una opción: "))

    if(opcion==1):
        numero1=int(input("Digita un número: "))
        numero2=int(input("Digita otro número: "))
        print(f'{numero1}+{numero2}={(numero1+numero2)}')

    elif(opcion==2):    
        numero1=int(input("Digita un número: "))
        numero2=int(input("Digita otro número: "))
        print(f'{numero1}-{numero2}={(numero1-numero2)}')

    elif(opcion==3):    
        numero1=int(input("Digita un número: "))
        numero2=int(input("Digita otro número: "))
        print(f'{numero1}*{numero2}={(numero1*numero2)}')

    elif(opcion==4):    
        numero1=int(input("Digita un número: "))
        numero2=int(input("Digita otro número: "))
        print(f'{numero1}/{numero2}={(numero1/numero2)}') 

    else:
        print("Digita una opción valida")           



opcion=0
print(" Menú a la carta")
print("*****************************************")

print("1 ---> Recibir votos")
print("1 ---> Mostrar votos")
print("0 ---> Salir")
print("*****************************************")


while(opcion!=0):
    opcion=int(input("Digita una opción: "))
    print(" Menú de votos")
    print("1 ---> Recibir votos")
    print("2 ---> Mostrar votos")
    print("0 ---> Salir")
    print("*****************************************")


    if(opcion==1):
       votoSenado=int(input("Digita la cantidad de votos por senado: ")) 
       votoSenado=votoSenado+votoSenado

    elif(opcion==2):  
        votoCamara=int(input("Digita la cantidad de votos por camara: ")) 
        votoCamara=votoCamara+votoCamara  

    elif(opcion==3):  
        votoConsulta=int(input("Digita la cantidad de votos por consulta: ")) 
        votoConsulta=votoConsulta+votoConsulta 

        print(" Menú de votos de consulta")
        print("1 ---> Pacto Historico")
        print("2 ---> Centro Esperanza")
        print("0 ---> Equipo Colombia")
        print("*****************************************") 




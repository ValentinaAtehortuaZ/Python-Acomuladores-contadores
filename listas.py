#Arreglos- siempre en plural
# un arreglo sirve para:
#1. Optimizar codigo
#2. Organizar codigo

#Listas

nombres=['juan','catalina','luis']
edades=[12,22,56]
descuentos=[False,True,False]


#Imprimiendo una lista
print(nombres)

#Accediendo a un elemento de la lista
print(nombres[0])

#Accediendo a los elementos de una lista

for nombre in nombres:
    print(nombre)

for edad in edades:
    print( edades )   

#Agregando elementos a una lista de python

nombres.append('martha')    
print(nombres)
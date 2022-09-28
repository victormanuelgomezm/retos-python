lista=[1,2,3,4]
print(lista[2])#acceder a una casilla de la lista
print([-1])#ultimo elemento de la lista
print([-2])#penultimo elemento de la lista
lista[0]=7# modificar un elemento de una posicion de la lista
print(lista)

for l in lista:#recorrer la lista y sumarle 1 
    print(l*2)

for index, l in enumerate(lista):
    print(f"en la posicion {index} se encuenta el valor {l}")#darle nombre a las filas


numeros=[5,9,10]
generos=["jazz", "rock", "djent"] #ponerle nombre a dos listas al mismo tiempo
for n1,g2 in zip(numeros, generos):
    print(f"el numero{n1} esta asociado con el genero {g2}")

    print(len(generos))

onces=["hamburguesa", "sandwich"," pizza"] # agrege posicion a lista 
onces.insert(2,"empanadas") # agregar elemento a ubicacion especifica
onces.extend(["malteada", "perro caliente"])
print(onces)
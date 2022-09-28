repeat="S"
alcancia=0
while repeat=="s" or repeat=="S":
    plata=int(input("ingrese el valor a ahorrar"))
    alcancia=alcancia+plata
    if alcancia<=100000:
        repeat=input(f"desea ingresar mas dinero s para si o n para no")
    else:
        break
print(f"su alcancia esta llena, el total ahorrado es {alcancia}")

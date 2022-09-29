from random import randint
saldo=0
repeat="SI"
repetir="si"
juego=0

while repeat=="si" or repeat=="SI":
    plata=int(input("ingrese el saldo que desea recargar  "))
    saldo=saldo+plata
    print("su saldo global es de ",saldo)
    if saldo>=0:
        repeat=input(f"si desea ingresar mas dinero escriba si de lo contrario escriba no \n")
    else:
        break
apuesta=int(input("ingrese el valor que desea apostar \n"))
while repetir=="si" or repetir=="SI":
    moneda=randint(1,2)
    eleccion=int(input("digite 1 para escoger cara y 2 para escoger sello "))
    if moneda==1 and eleccion==1:
        saldo=saldo+apuesta
        juego=juego+1
        print("salio cara, usted escogio cara ganaste!! , debes duplicar tu apuesta")
    elif moneda==1 and eleccion==2:
        saldo=saldo-apuesta
        juego=juego+1
        print("salio cara, usted escogio sello perdiste!!")
        if saldo>0:
            print("puede seguir jugando")
        elif saldo<0:
            print("saldos insuficientes")
        else:
            break
    elif moneda==2 and eleccion==2:
        saldo=saldo+apuesta
        juego=juego+1
        print("salio sello, usted escogio sello ganaste!! , debes duplicar tu apuesta")
    elif moneda==2 and eleccion==1:
        saldo=saldo-apuesta
        juego=juego+1
        print("salio sello, usted escogio cara perdiste!!")
        if saldo>0:
            print("puede seguir jugando")
        elif saldo<0:
            print("saldos insuficientes")
        else:
            break
    elif eleccion!=1 or eleccion!=2:
        print("digitaste una opcion incorrecta")
    else:
        print("datos incorrectos")
    print(f" su saldo actual es ",saldo)
    repetir=input(f"quiere jugar de nuevo escriba si o de lo contario esbriba no \n")
    if repetir=="si" or repetir=="SI":
        apuesta=int(input("ingrese el valor que desea apostar \n"))
    else:
        break
print("el numero de veces que usted jugo fue",juego,"el dinero acumulado fue",saldo)


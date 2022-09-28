from random import randint


juego=randint(1,3)
eleccion=int(input("digite 1 para escoger piedra y 2 para escoger papel y 3 para escoger tijera "))
if juego==1 and eleccion==1:
    print("salio piedra, usted escogio piedra, empate!!")
elif juego==1 and eleccion==2:
    print("salio piedra, usted escogio papel, ganaste!!")
elif juego==1 and eleccion==3:
    print("salio piedra, usted escogio tijera, perdiste!!")
elif juego==2 and eleccion==1:
    print("salio papel, usted escogio piedra, perdiste!!")
elif juego==2 and eleccion==2:
    print("salio papel, usted escogio papel, empate!!")
elif juego==2 and eleccion==3:
    print("salio papel, usted escogio tijera, ganaste!!")
elif juego==3 and eleccion==1:
    print("salio tijera, usted escogio piedra, ganaste!!")
elif juego==3 and eleccion==2:
    print("salio tijera, usted escogio papel, perdiste!!")
elif juego==3 and eleccion==3:
    print("salio tijera, usted escogio tijera, empate!!")
else:
    print("datos incorrectos")
print(f"el juego escogio {juego}")
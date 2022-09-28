from random import randint


craps=randint(1,6)
craps2=randint(1,6)
print("lanza los dados si sale un par 1 en los dados \n un total de 3 en los dados \n un total de 11 en los dados \n si obtiene 2 o 12 en los dados \n un total de 7 en los dados ganaste!!")
print(f"lanzar los dados {craps,craps2}")
if craps==1 and craps2==1:
    print("si sale un par de 1, ganaste!!")
elif craps==1 and craps2==2 or craps==2 and craps2==1:
    print("si sale un total de 3, ganaste!!")
elif craps==6 and craps2==5 or craps==5 and craps2==6:
    print("si sale un total de 11, ganaste!!")
elif craps==1 and craps2==1 or craps==6 and craps2==6:
    print("si el resultado es 2 o 12, ganaste!!")
elif craps==2 and craps2==5 or craps==5 and craps2==2 or craps==4 and craps2==3 or craps==3 and craps2==4:
    print("si el resultado es 7, ganaste!!")
else:
    print("el resultadoes diferente, perdiste!!")
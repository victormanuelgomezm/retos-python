hombre=0
mujer=0
seleccion=(1,2)
for i in range(1,11,1):
    seleccion=int(input("ingrese con que genero te identificas, 1 para hombre o 2 para mujer "))
    if seleccion==1:
        hombre=hombre+1
        total1=hombre
        print("usted escogio hombre")
    elif seleccion==2:
        mujer=mujer+1
        total=mujer
        print("usted escogio mujer")
else:
    print("la cantidad de hombres en el grupo son", total, "la cantidad de mujeres en el grupo es", total1)


   
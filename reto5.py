from random import randint

compra=int(input("ingrese el valor de su compra \n"))
descuento=randint(1,4)
if compra>50000:
    print("salio escogido/a para participar en nuestra promocion de aniversario")
    if descuento==1:
        procedimiento=compra*0.10
        total=compra-procedimiento
        print("salio bolita roja, su descuento es del 10% en el valor de su factura, su total a pagar es",total)
    elif descuento==2:
        procedimiento=compra*0.30
        total=compra-procedimiento
        print("salio bolita azul, su descuento es de 30% en el valor de su factura,su total a pagar es",total)
    elif descuento==3:
        procedimiento=compra*0.50
        total=compra-procedimiento
        print("salio bolita amarilla, su descuento es de 50% en el valor de su factura,su total a pagar es ",total)
    elif descuento==4:
        print("salio bolita blanca, te llevas tu compra gratis")
    else:
        print(f"el juego escogio{descuento}")
else:
    print("no fue escogido/a para participar en nuestra promocion, su total a pagar es ",compra)
    
    

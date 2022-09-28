from random import randint
election=int(input("oprima 1 para ingresar el valor de su factura o oprima 2 para ingresar la cantidad de productos comprados \n"))
if election==1:
    compra=int(input("ingrese el valor de su compra \n"))
else:
    numproductos=int(input("ingrese el numero de productos a comprar "))
    valorproducto=10000
    compra=numproductos*valorproducto

descuento=randint(1,4)
total=compra
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
if descuento==1 or descuento==2 or descuento==3:
    valorrecibido=int(input("igrese el valor con el que desea cancelar "))
    cambio=valorrecibido-total
    print ("su compra fue de ",total," productos me realizo el pago con ",valorrecibido," su cambio es ",cambio)
else: 
    descuento==4
    print("ganaste")
    


    
    

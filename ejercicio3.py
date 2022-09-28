for i in range(1,4,1):
    precio=int(input("ingrese el precio del producto"))
    cantidad=int(input("ingrese la cantidad del producto"))
    subtotal=precio*cantidad
    total=total+subtotal
    print(f"el costo del producto es {total}")
print("el costo del desayuno es ", total)
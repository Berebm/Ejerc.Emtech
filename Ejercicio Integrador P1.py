#Ejercicio integrador Parte 1

ventaProductos = [
[2, 122],
[1, 89],
[1, 22],
[3, 48],
[1, 75],
[3, 322],
[2, 95],
[1, 148],
[1, 83],
[3, 100]
]
costoEnvio = 1500
venta = 0
totalCajasVendidas = 0
ventaDia = 0
productosMatriz = [[1, "Maiz grano", 285.55], 
        [2,"Pepino",334.72], 
        [3,"Tomate verde",129.00]]
print("Introduzca el id del producto")
idProducto = int(input())
if(idProducto > 3):
    print("No existe ese producto")
    sys.exit()
else:
    if (idProducto >= 1):
        idProducto = idProducto-1
    else:
        print("No existe ese producto")
    productosMatriz = productosMatriz[idProducto]
    producto = productosMatriz[1]
    precio = productosMatriz[2]
    print("El producto es: " + producto)
    print("El precio por caja es: " + str(precio))
    idProducto = idProducto+1
    for n in ventaProductos:
        if(int(n[0]) == idProducto):
            cajasVendidas  = int(n[1])
            totalCajasVendidas = totalCajasVendidas + cajasVendidas
            if (cajasVendidas <= 100):
                ventaTotalCajas = (cajasVendidas * precio + costoEnvio)
            else:
                ventaTotalCajas = (cajasVendidas * precio) 

if(totalCajasVendidas > 1500):
    print("Aplica descuento del 20%")
else:
    print("No aplica descuento del 20%")
print("El costo total a pagar: " + str(ventaTotalCajas))
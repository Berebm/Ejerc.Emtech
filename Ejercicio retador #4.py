#Ejercicio retador 4
import sys
costoEnvio = 1500
total = 0
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
    print("Introduzca la cantidad de cajas a vender")
    cajasVender = int(input())
    producto = productosMatriz[1]
    precio = int(productosMatriz[2])
    if(cajasVender <= 100):
        total = (precio * cajasVender + costoEnvio)
        print("Se cobra envio de " + str(costoEnvio))
    else:
        total = (precio * cajasVender)
print("El producto es " + producto)
print("El precio es " + str(precio))
print("El total es " + str(total))
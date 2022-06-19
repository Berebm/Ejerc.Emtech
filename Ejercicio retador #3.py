#Ejercicio retador 3
material = input("Ingrese el material que desea transportar: ")

pesoXcostal = input("Ingrese el peso de su material: ")

Envio = int(pesoXcostal) > int(1627) and int(pesoXcostal) < int(3254)

print("¿Es posible realizar el envio de " + str(material)+"? " + str(Envio))

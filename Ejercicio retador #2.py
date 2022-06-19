#Ejercicio Retador 2
municipio = input("Ingrese el nombre de su municipio: ")
numhabitantes = input("Ingrese el numero de habitantes: ")

municipio1 = input("Ingrese el nombre de su municipio: ")
numhabitantes1 = input("Ingrese el numero de habitantes: ")

municipio2 = input("Ingrese el nombre de su municipio: ")
numhabitantes2 = input("Ingrese el numero de habitantes: ")

municipios = [municipio, municipio1, municipio2]
habitantes = [int(numhabitantes), int(numhabitantes1), int(numhabitantes2)]

totalHabitantes = sum(habitantes)
promedioHabitantes = float(totalHabitantes) / 3

print("La cantidad de habitantes es: " + str(totalHabitantes))

print("El promedio es de: " + str(promedioHabitantes))

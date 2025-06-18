import random
import math

hogares = ["Familia Soto", "Familia Morales", "Familia Vásquez", "Familia Rojas", "Familia González", "Familia Castillo", "Familia Bravo", "Familia Contreras", "Familia Jara", "Familia Lagos", "Familia Palma", "Familia Reyes"]
hogares2 = {}

def asignar_consumo():
    for x in hogares:
        consumo = random.randint(8000, 30000)
        hogares2[x] = consumo
    print("Asignacion aleatoria de consumo realizada!")

def clasificar_consumo():
    clasificacion = ""
    for x, y in hogares2.items():
        if y < 12000:
            clasificacion = "Menores a 12.000 litros"
        elif y >= 12000 and y <= 25000:
            clasificacion = "Entre 12.000 y 25.000 litros"
        else:
            clasificacion = "Mayores a 25.000 litros"
        print(f"Hogar: {x}\nConsumo: {y}\nClasificacion: {clasificacion}\n---")
        hogares2[x] = y, clasificacion

def ver_stats():
    mayor = 0
    menor = None
    for x, y in hogares2.values():
        if x > mayor:
            mayor = x
        if menor == None or x < menor:
            menor = x
    valores = [i[0] for i in hogares2.values()]
    promedio = sum(valores) / len(valores)

    total= math.prod(valores)
    n = len(valores)
    media_geometrica = total ** (1/n)
    print(f"El consumo maximo fue de: {mayor:.2f} litros")
    print(f"El consumo minimo fue de: {menor:.2f} litros")
    print(f"El promedio de consumo fue de: {promedio:.2f} litros")
    print(f"La media geometrica fue de: {media_geometrica:.2f} litros")

def reporte_detallado():
    total = 0
    for x, y in hogares2.items():
        cantidad = y[0]
        total += cantidad
    subsidio = total * 0.05
    impuesto = total * 0.07
    neto = total - subsidio - impuesto

    print(f"Consumo bruto: {total:.2f}\nDescuento por subsidio: {subsidio:.2f}\nImpuesto: {impuesto:.2f}\nConsumo neto: {neto:.2f}")

def salir():
    print("Nombre: Melissa Figueroa\nRut: #####\nCarrera: Ingenieria en Informatica")

def menu():
    opcion = 0
    while opcion != 5:
        print("---Control de Consumo De Agua En Hogares---\n1.Asignar consumo aleatorio\n2.Clasificar consumo\n3.Estadisticas\n4.Reporte detallado\n5.Salir.")
        while True:
            try:
                opcion = int(input(""))
                if opcion >= 1 and opcion <= 5:
                    break
                else:
                    print("Introduce una opcion valida entre 1-5")
            except ValueError:
                print("Introduce un digito valido")
        if opcion == 1:
            asignar_consumo()
        elif opcion == 2:
            clasificar_consumo()
        elif opcion == 3:
            ver_stats()
        elif opcion == 4:
            reporte_detallado()
        elif opcion == 5:
            salir()


menu()
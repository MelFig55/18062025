huertos = ["Huerto Norte", "Huerto Sur", "Huerto Este", "Huerto Oeste", 
"Huerto Central", "Huerto 1", "Huerto 2", "Huerto 3", "Huerto 4", "Huerto 5"]

huertos2= {}

import random 
import math

produccion = random.randint(5000, 50000)

def generar_produccion():
    for x in huertos:
        produccion = random.randint(5000, 50000)
        huertos2[x] = produccion

def clasificar_produccion():
    for x, y in huertos2.items():
        clasificacion = ""
        if y < 10000:
            clasificacion = "menor a 10.000kg"
        elif y >= 10000 and y <= 30000:
            clasificacion = "entre 10.000 y 30.000 kg"
        elif y >= 30000:
            clasificacion = "mayor a 30.000 kg"
        print(f"{x}: {y}, {clasificacion}")
        huertos2[x] = y, clasificacion

def ver_stats():
    mayor = 0
    menor = 51000
    for x, y in huertos2.values():
        if x > mayor:
            mayor = x
        if menor == 51000 or x < menor:
            menor = x
    valores = [i[0] for i in huertos2.values()]
    promedio = sum(valores) / len(valores)

    total= math.prod(valores)
    n = len(valores)
    media_geometrica = total ** (1/n)

    print(f"La produccion maxima es: {mayor} ")
    print(f"La produccion menor es: {menor}")
    print(f"La produccion en promedio es: {promedio}")
    print(f"La media geometrica es: {media_geometrica:.2f}")

def reporte():
    total = 0
    for x, y in huertos2.items():
        cantidad = y[0]
        print(f"huerto: {x}, cantidad: {cantidad}")
        total += cantidad
    
    transporte = total * 0.05
    embalaje = total * 0.03
    neta = total - transporte - embalaje
    
    print(f"Produccion total: {total:.2f}")
    print(f"Descuento por transporte[5%]: {transporte:.2f}")
    print(f"Descuento por embalaje[3%]: {embalaje:.2f}")
    print(f"Produccion neta: {neta:.2f}")

def salir():
    print("Nombre: Melissa Figueroa\nRut: #####\nCarrera: Ingenieria en Informatica")


def menu():
    opcion = 0

    while opcion != 5:
        print("---Analisis de produccion agricola---\n1.Generar produccion aleatoria.\n2.Clasificar produccion\n3.Ver estadisticas.\n4.Reporte detallado\n5.Salir.")
        while True:
            try:
                opcion = int(input(""))
                if opcion in [1, 2, 3, 4, 5]:
                    break
                else:
                    print("Introduce una opcion valida entre [1-5]")
            except ValueError:
                print("Introduce un digito valido.")

        if opcion == 1:
            generar_produccion()
        elif opcion == 2:
            clasificar_produccion()
        elif opcion == 3:
            ver_stats()
        elif opcion == 4:
            reporte()
        elif opcion == 5:
            salir()

menu()
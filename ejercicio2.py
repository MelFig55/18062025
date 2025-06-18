import random
import math

vendedores = ["Camila Soto", "Esteban Ruiz", "Daniela Pérez", "Jorge Vargas", "Soledad Acuña", "Felipe Campos", "Laura Silva", "Marcelo Torres"]

vendedores2 = {}
def generar_ventas():
    for x in vendedores:
        valor = random.randint(200000, 2000000)
        vendedores2[x] = valor

def clasificar_ventas():
    clasificacion = ""
    for x, y in vendedores2.items():
        if y < 500000:
            clasificacion = "Menores a $500.000"
        elif y >= 500000 and y <= 1200000:
            clasificacion = "Entre $500.000 y $1.200.000"
        else:
            clasificacion = "Mayores a $1.200.000"
        print(f"Vendedor: {x}, Ventas: {y}, Clasificacion: {clasificacion}")
        vendedores2[x] = y, clasificacion

def ver_stats():
    mayor = 0
    menor = None
    for x, y in vendedores2.values():
        if x > mayor:
            mayor = x
        if menor == None or x < menor:
            menor = x
    valores = [i[0] for i in vendedores2.values()]
    promedio = sum(valores) / len(valores)

    total= math.prod(valores)
    n = len(valores)
    media_geometrica = total ** (1/n)

    print(f"La venta maxima es: {mayor} ")
    print(f"La venta menor es: {menor}")
    print(f"La venta en promedio es: {promedio}")
    print(f"La media geometrica es: {media_geometrica:.2f}")

def reporte_comisiones():
    total = 0
    for x, y in vendedores2.items():
        cantidad = y[0]
        comision = cantidad * 0.10
        impuesto = cantidad * 0.08
        neto = y[0] - comision - impuesto
        print(f"Vendedor: {x}\nComision por venta: ${comision:.2f}\nImpuesto: ${impuesto:.2f}\nNeto: ${neto:.2f}\n---")    
    transporte = total * 0.05
    embalaje = total * 0.03
    neta = total - transporte - embalaje

def salir():
    print("Nombre: Melissa Figueroa\nRut: #####\nCarrera: Ingenieria en Informatica")

def menu():
    opcion = 0
    while opcion != 5:
        print("---Control de ventas de una libreria---\n1.Generar ventas aleatorias\n2.Clasificar ventas\n3.Estadisticas generales.\n4.Reporte completo de comisiones\n5.Salir.")
        while True:
            try:
                opcion = int(input(""))
                if opcion >= 1 and opcion <= 5:
                    break
                else:
                    print("Ingresa una opcion valida entre [1-5]")
            except ValueError:
                print("Ingresa un digito valido.")
        
        if opcion == 1:
            generar_ventas()
        elif opcion == 2:
            clasificar_ventas()
        elif opcion == 3:
            ver_stats()
        elif opcion == 4:
            reporte_comisiones()
        elif opcion == 5:
            salir()

menu()
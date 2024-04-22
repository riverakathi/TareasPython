def calcular_capital(cantidad, interes, años):
    capital = cantidad
    for año in range(1, años + 1):
        capital += capital * (interes / 100)
        print(f"Capital tras {año} año(s): {capital:.2f}")

# Solicitar al usuario la cantidad, el interés y el número de años
cantidad = float(input("¿Cantidad a invertir?: "))
interes = float(input("¿Interés porcentual anual?: "))
años = int(input("¿Años?: "))

# Calcular y mostrar el capital obtenido cada año
calcular_capital(cantidad, interes, años)

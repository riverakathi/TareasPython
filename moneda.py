def convertir_a_monedas(cantidad):
    # Inicializamos el diccionario de monedas con sus respectivos valores
    monedas = {
        20: 0,
        10: 0,
        5: 0,
        1: 0
    }

    # Calculamos el número de monedas de cada valor
    for valor, cantidad_monedas in monedas.items():
        monedas[valor] = cantidad // valor
        cantidad %= valor

    # Imprimimos el resultado
    for valor, cantidad_monedas in monedas.items():
        print(f"Monedas de ${valor}: {cantidad_monedas}")

# Solicitamos al usuario que ingrese la cantidad a convertir
cantidad_a_convertir = int(input("Cantidad a Convertir: "))

# Llamamos a la función para convertir la cantidad en monedas
convertir_a_monedas(cantidad_a_convertir)

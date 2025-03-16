import random

# Inicializar datos del jugador
jugador = {
    "saldo": 100,
    "apuestas": [],
    "ganancias": [],
    "exitos": 0,
    "fracasos": 0
}

# Función para realizar una apuesta
def apostar(tipo, valor, cantidad):
    if cantidad > jugador["saldo"]:
        print("No tienes saldo suficiente para esta apuesta.")
        return
    jugador["saldo"] -= cantidad
    resultado = random.randint(1, 36)  # Resultado de la ruleta
    color = "rojo" if resultado % 2 == 0 else "negro"
    seccion = (resultado - 1) // 12 + 1  # Secciones: 1-12, 13-24, 25-36

    exito = False
    if tipo == "número" and valor == resultado:
        ganancias = cantidad * 20
        exito = True
    elif tipo == "sección" and valor == seccion:
        ganancias = cantidad * 5
        exito = True
    elif tipo == "color" and valor == color:
        ganancias = cantidad * 2
        exito = True
    else:
        ganancias = 0

    jugador["apuestas"].append(cantidad)
    jugador["ganancias"].append(ganancias)
    if exito:
        jugador["saldo"] += ganancias
        jugador["exitos"] += 1
        print("¡Ganaste!", ganancias, "coins.")
    else:
        jugador["fracasos"] += 1
        print("Perdiste esta vez. El resultado fue:", resultado, "-", color)

# Función para consultar el estado del jugador
def consultar():
    print("\nSaldo total:", jugador["saldo"])
    print("Cantidad total apostada:", sum(jugador["apuestas"]))
    print("Cantidad total ganada:", sum(jugador["ganancias"]))
    total_apuestas = jugador["exitos"] + jugador["fracasos"]
    if total_apuestas > 0:
        promedio_exito = jugador["exitos"] / total_apuestas
    else:
        promedio_exito = 0
    print("Promedio de éxito:", promedio_exito)

# Menú principal
while True:
    print("\n=== Ruleta ===")
    print("1. Apostar")
    print("2. Consultar estado")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        tipo = input("¿Qué tipo de apuesta deseas hacer? (número/sección/color): ").lower()
        valor = input("Indica el valor (número entre 1 y 36, sección 1-3, rojo/negro): ")
        if tipo == "número" or tipo == "sección":
            valor = int(valor)
        cantidad = int(input("¿Cuánto deseas apostar?: "))
        apostar(tipo, valor, cantidad)
    elif opcion == "2":
        consultar()
    elif opcion == "3":
        print("Gracias por jugar. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
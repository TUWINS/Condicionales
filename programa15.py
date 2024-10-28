# Función para determinar el ganador
def determinar_ganador(opcion1, opcion2):
    if opcion1 == opcion2:
        return "Empate"
    elif (opcion1 == "piedra" and opcion2 == "tijera") or \
         (opcion1 == "tijera" and opcion2 == "papel") or \
         (opcion1 == "papel" and opcion2 == "piedra"):
        return "Gana Jugador 1"
    else:
        return "Gana Jugador 2"

# Función principal del juego
def juego_piedra_papel_tijera():
    opciones_validas = ["piedra", "papel", "tijera"]
    
    jugador1 = input("Jugador 1, introduce tu elección (piedra, papel o tijera): ").lower()
    if jugador1 not in opciones_validas:
        print("Opción incorrecta para Jugador 1")
        return

    jugador2 = input("Jugador 2, introduce tu elección (piedra, papel o tijera): ").lower()
    if jugador2 not in opciones_validas:
        print("Opción incorrecta para Jugador 2")
        return

    resultado = determinar_ganador(jugador1, jugador2)
    print(resultado)

# Ejecutar el juego
juego_piedra_papel_tijera()

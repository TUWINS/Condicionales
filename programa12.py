# Función para convertir el número a letras
def numero_a_letras(numero):
    numeros_letras = {
        1: "uno",
        2: "dos",
        3: "tres",
        4: "cuatro",
        5: "cinco",
        6: "seis"
    }
    return numeros_letras.get(numero, "ERROR")

# Función para obtener la cara opuesta del dado
def cara_opuesta(numero):
    opuestas = {
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return opuestas.get(numero, None)

# Solicitar el número del dado al usuario
resultado = int(input("Introduce el resultado del dado (1-6): "))

# Verificar si el número es válido y mostrar la cara opuesta
if 1 <= resultado <= 6:
    opuesto = cara_opuesta(resultado)
    print(f"La cara opuesta al {resultado} es {numero_a_letras(opuesto)}")
else:
    print("ERROR: número incorrecto.")

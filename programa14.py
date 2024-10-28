# Función para obtener el número de días del mes
def dias_en_mes(numero):
    meses = {
        1: 31,  # Enero
        2: 28,  # Febrero (sin considerar años bisiestos)
        3: 31,  # Marzo
        4: 30,  # Abril
        5: 31,  # Mayo
        6: 30,  # Junio
        7: 31,  # Julio
        8: 31,  # Agosto
        9: 30,  # Septiembre
        10: 31, # Octubre
        11: 30, # Noviembre
        12: 31  # Diciembre
    }
    return meses.get(numero, "ERROR: número incorrecto.")

# Solicitar el número del mes al usuario
numero_mes = int(input("Introduce un número entero entre 1 y 12: "))

# Obtener y mostrar el número de días del mes correspondiente
resultado = dias_en_mes(numero_mes)
print(resultado)

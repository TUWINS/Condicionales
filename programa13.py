# Función para convertir el número del día a su nombre correspondiente
def numero_a_dia(numero):
    dias_semana = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    return dias_semana.get(numero, "ERROR: número incorrecto.")

# Solicitar el número del día al usuario
dia = int(input("Introduce el día de la semana (1-7): "))

# Mostrar el día correspondiente o un mensaje de error
resultado = numero_a_dia(dia)
print(resultado)

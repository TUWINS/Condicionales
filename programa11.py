# Función para calcular el costo base de la llamada según su duración
def calcular_costo_base(duracion):
    if duracion <= 5:
        return duracion * 1.00
    elif duracion <= 8:
        return 5 * 1.00 + (duracion - 5) * 0.80
    elif duracion <= 10:
        return 5 * 1.00 + 3 * 0.80 + (duracion - 8) * 0.70
    else:
        return 5 * 1.00 + 3 * 0.80 + 2 * 0.70 + (duracion - 10) * 0.50

# Solicitar la duración de la llamada al usuario
duracion = int(input("Introduce la duración de la llamada en minutos: "))

# Solicitar el día de la semana y el turno al usuario
dia = input("Introduce el día de la semana (lunes a domingo): ").lower()
turno = input("Introduce el turno (mañana/tarde): ").lower()

# Calcular el costo base de la llamada
costo_base = calcular_costo_base(duracion)

# Calcular el impuesto según el día y el turno
if dia == "domingo":
    impuesto = 0.03
elif turno == "mañana":
    impuesto = 0.15
else:
    impuesto = 0.10

# Calcular el costo total
costo_total = costo_base * (1 + impuesto)

# Mostrar los resultados
print(f"Costo base de la llamada: {costo_base:.2f} euros")
print(f"Impuesto aplicado: {impuesto * 100:.0f}%")
print(f"Costo total de la llamada: {costo_total:.2f} euros")

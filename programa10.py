# Solicitar el número de alumnos al usuario
num_alumnos = int(input("Introduce el número de alumnos: "))

# Calcular el costo por alumno y el pago a la compañía de autobuses
if num_alumnos >= 100:
    costo_por_alumno = 65
    pago_compania = num_alumnos * costo_por_alumno
elif 50 <= num_alumnos <= 99:
    costo_por_alumno = 70
    pago_compania = num_alumnos * costo_por_alumno
elif 30 <= num_alumnos <= 49:
    costo_por_alumno = 95
    pago_compania = num_alumnos * costo_por_alumno
else:
    costo_por_alumno = 4000 / num_alumnos
    pago_compania = 4000

# Mostrar el resultado
print(f"El pago a la compañía de autobuses es de {pago_compania} euros.")
print(f"Cada alumno debe pagar {costo_por_alumno:.2f} euros.")

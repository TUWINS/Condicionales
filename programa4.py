# Solicitar los dos números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Comprobar si el segundo número es cero
if num2 != 0:
    division = num1 / num2
    print(f"La división de {num1} entre {num2} es {division}")
else:
    print("No se puede dividir por cero. Por favor, introduce un número diferente de cero.")

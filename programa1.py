# Solicitar dos números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Comparar los dos números y mostrar el resultado
if num1 > num2:
    print(f"El número mayor es: {num1}")
elif num2 > num1:
    print(f"El número mayor es: {num2}")
else:
    print("Son iguales")

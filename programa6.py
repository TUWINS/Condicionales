# Solicitar una cadena al usuario
cadena = input("Introduce una cadena: ")

# Comprobar si la cadena es una letra mayúscula
if len(cadena) == 1 and cadena.isupper() and cadena.isalpha():
    print("La cadena es una letra mayúscula")
else:
    print("La cadena no es una letra mayúscula")

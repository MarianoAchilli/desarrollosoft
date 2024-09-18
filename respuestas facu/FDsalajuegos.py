edad = int(input("Ingrese la edad del cliente: "))
precio_entrada = 0

if edad < 4:
    precio_entrada = "GRATIS"
elif edad >= 4 and edad < 18:
    precio_entrada = "€5"
else:
    precio_entrada = "€10"
print(f"El valor de su entrada es: {precio_entrada}")
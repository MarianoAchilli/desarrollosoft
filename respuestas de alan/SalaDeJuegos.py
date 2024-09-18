edad = int(input("Ingrese su edad: "))

if edad <= 4:
    print("La entrada es gratis.")
elif edad > 4 and edad < 18:
    print("El valor de la entrada es: 5€")
else:
    print("El valor de la entrada para mayores a 18 es: 10€")
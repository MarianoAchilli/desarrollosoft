edad = int(input("Ingrese su edad: "))
sueldo = int(input("Ingrese su sueldo: "))

if edad > 16 and sueldo >= 1000:
    print("El usuario tiene que tributar impuestos")
else:
    print("El usuario no tiene que tributar impuestos")
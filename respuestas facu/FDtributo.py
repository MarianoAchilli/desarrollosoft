edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales: "))
if edad < 16 or ingresos < 1000:
    print("Usted no debe tributar")
else:
    print("Usted debe tributar")
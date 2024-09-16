# Leer la calificación del estudiante
calificacion = float(input("Ingrese la calificación del estudiante (0-100): "))

# Determinar la calificación final usando sentencias if
if calificacion >= 90:
    resultado = "Excelente"
elif calificacion >= 80:
    resultado = "Muy Bueno"
elif calificacion >= 70:
    resultado = "Bueno"
elif calificacion >= 60:
    resultado = "Suficiente"
else:
    resultado = "Insuficiente"

# Imprimir el resultado
print(f"La calificación final es: {resultado}")


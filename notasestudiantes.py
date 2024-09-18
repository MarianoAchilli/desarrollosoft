nota1 = float(input("introduzca la nota 1: "))
nota2 = float(input("introduzca la nota 2: "))
nota3 = float(input("introduzca la nota 3: "))
#la cantidad de faltas para no aprobar es de 10 clases
asistencias = int(input("Ingrese la cantidad de faltas: "))
promedio = (nota1 + nota2 + nota3) / 3

if promedio > 6 and asistencias < 10:
    print(f"el estudiante aprobo con el promedio de: {promedio:.2f}")
elif promedio > 8 and asistencias < 10:
    print(f"el estudiante promociono la materia con un promedio de: {promedio:.2f}")
else:
    print(f"El estudiante no aprobo la materia {promedio:.2f}")
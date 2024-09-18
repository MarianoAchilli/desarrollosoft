nota1 = float(input("Ingrese la nota de su primer exámen: "))
nota2 = float(input("Ingrese la nota de su segundo exámen: "))
nota3 = float(input("Ingrese la nota de su tercer exámen: "))
promedio = (nota1 + nota2 + nota3)/3
asistencia = int(input(f"Ingrese su porcentaje de asistencia a clases: "))

if promedio < 6 or asistencia < 75:
    print("Usted ha reprobado la materia y debe recursarla")
elif promedio >= 6 and promedio < 8 and asistencia >= 75:
    print("Usted ha regularizado la materia y está habilitado para rendir el exámen final.")
elif promedio >= 8 and asistencia >= 75:
    print("Usted ha conseguido la aprobación directa de la materia")
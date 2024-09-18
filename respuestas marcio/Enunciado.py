def determine_membresia():
    edad = int(input("Ingrese su edad: "))
    genero = input("Ingrese su género (hombre/mujer): ")

    if genero.lower() == "hombre":
        if edad < 18:
            membresia = "No elegible"
        elif 18 <= edad <= 30:
            membresia = "Estudiante"
        elif 31 <= edad <= 60:
            membresia = "Adulto"
        else:
            membresia = "Senior"
    elif genero.lower() == "mujer":
        if edad < 18:
            membresia = "No elegible"
        elif 18 <= edad <= 30:
            membresia = "Estudiante Femenino"
        elif 31 <= edad <= 60:
            membresia = "Adulto Femenino"
        else:
            membresia = "Senior Femenino"
    else:
        membresia = "No elegible"

    print("Su tipo de membresía es:", membresia)

# Llamada a la función
determine_membresia()
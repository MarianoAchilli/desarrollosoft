# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

try:

    nombre=str(input("Ingrese su nombre: ")).lower()
    sexo=str(input("Ingrese su sexo: Masculino | Femenino: ")).lower()

    if nombre[0]>="a" and nombre[0]<="m" and sexo=="femenino" or nombre[0]>='n' and nombre[0]<='z' and sexo=="masculino": 
            print ("Usted será parte del grupo A.")

    elif nombre[0]>="n" and nombre[0]<="z" and sexo=="femenino" or nombre[0]>="a" and nombre[0]<="m" and sexo=="masculino": 
            print ("Usted será parte del grupo B.")

    else:
           raise ValueError ("Datos no válidos. Por favor, intente otra vez.")
    
except ValueError as e:
       print (f"ERROR: {e}")

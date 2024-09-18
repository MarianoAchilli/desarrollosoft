platillo = (input("Ingrese el tipo de platillo elegido(Vegetariano, Carne o Pescado): ")).upper()
bebida = (input("Va a pedir bebida? \"S\" para SÍ, \"N\" para NO: ")).upper()
postre = (input("Va a pedir postre? \"S\" para SÍ, \"N\" para NO: ")).upper()
PRECIO_VEGETARIANO = 100
PRECIO_PESCADO = 250
PRECIO_CARNE = 500
PRECIO_BEBIDA = 5
PRECIO_POSTRE = 7
PRECIO_BYP = 10

match platillo:
    case "VEGETARIANO":
        if bebida == "S" and postre == "S":
            print(f"Su platillo tiene un costo de ${PRECIO_VEGETARIANO + PRECIO_BYP}")
        elif bebida == "S" and postre == "N":
            print(f"Su platillo tiene un costo de ${PRECIO_VEGETARIANO + PRECIO_BEBIDA}")
        elif bebida == "N" and postre == "S":
            print(f"Su platillo tiene un costo de ${PRECIO_VEGETARIANO + PRECIO_POSTRE}")
        else:
            print(f"Su platillo tiene un costo de ${PRECIO_VEGETARIANO}")
    case "CARNE":
        if bebida == "S" and postre == "S":
            print(f"Su platillo tiene un costo de ${PRECIO_CARNE + PRECIO_BYP}")
        elif bebida == "S" and postre == "N":
            print(f"Su platillo tiene un costo de ${PRECIO_CARNE + PRECIO_BEBIDA}")
        elif bebida == "N" and postre == "S":
            print(f"Su platillo tiene un costo de ${PRECIO_CARNE + PRECIO_POSTRE}")
        else:
            print(f"Su platillo tiene un costo de ${PRECIO_CARNE}")
    case "PESCADO":
        if bebida == "S" and postre == "S":
            print(f"Su platillo tiene un costo de ${PRECIO_PESCADO + PRECIO_BYP}")
        elif bebida == "S" and postre == "N":
            print(f"Su platillo tiene un costo de ${PRECIO_PESCADO + PRECIO_BEBIDA}")
        elif bebida == "N" and postre == "S":
            print(f"Su platillo tiene un costo de ${PRECIO_PESCADO + PRECIO_POSTRE}")
        else:
            print(f"Su platillo tiene un costo de ${PRECIO_PESCADO}")
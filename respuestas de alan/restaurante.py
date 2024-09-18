valor = 0
Eleccion = int(input("ingrese el platillo que desea 1-vegetariano, 2-carne, 3-pescado: "))
match Eleccion:
    case 1: 
        valor = 15
        bebida = int(input("¿Quiere una bebida? (Si:1/No:2): "))
        if bebida == 1:
            valor += 5
        print(f"el valor total es de. {valor}")
    case 2:
        valor = 30
        postre = int(input("quiere un postre? (Si:1/No:2): "))
        if postre == 1:
            valor += 7
        print(f"el valor total es de: {valor}")
    case 3:
        valor = 45
        PostreYBebida = int(input("quiere postre y bebida? (Si:1/No:2): "))
        if PostreYBebida == 1:
            valor += 10
        print(f"el valor total es de: {valor}")



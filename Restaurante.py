# Un restaurante ofrece un menú especial con tres tipos de platillos: vegetariano, de carne y de pescado. 
# Cada uno tiene un precio base de $100, pero dependiendo de las opciones adicionales, el precio final puede variar:

# Si el cliente elige un platillo vegetariano y también quiere una bebida, se le añade $5 al precio base del platillo.
# Si el cliente elige un platillo de carne y también quiere postre, se le añade $7 al precio base del platillo.
# Si el cliente elige un platillo de pescado y además quiere ambos, bebida y postre, se le añaden $10 al precio base del platillo.
# Si el cliente no elige ninguna opción adicional, el precio no varía.

# Escribe un programa que reciba como entrada:
# El tipo de platillo seleccionado (vegetariano, carne o pescado).
# Si el cliente quiere bebida (sí/no).
# Si el cliente quiere postre (sí/no).
# El programa debe calcular y mostrar el precio final del platillo según las reglas descritas.

PRECIO_BASE=100

print ("Elija un tipo de platillo.")
print ("1. Vegetariano - 2. Carne - 3. Pescado")
tipo_plato=int(input("Ingrese el tipo de platillo que desea: "))

if tipo_plato==1:
    print ("1. Si - 2. No")
    bebida=int(input("¿Ud. quiere una bebida? "))
    if bebida==1:
        print (f"El precio final de su platillo es de ${PRECIO_BASE+5}.")
    elif bebida==2:
        print (f"El precio final de su platillo es de ${PRECIO_BASE}.")
else:
    if tipo_plato==2:
        print ("1. Si - 2. No")
        postre=int(input("¿Ud. quiere un postre? "))
        if postre==1:
            print (f"El precio final de su platillo es de {PRECIO_BASE+7}.")
        elif postre==2:
            print (f"El precio final de su platillo es de {PRECIO_BASE}.")
    elif tipo_plato==3:
        print ("1. Si - 2. No")
        bebida_postre=int(input("¿Ud. quiere bebida y postre? "))
        if bebida_postre==1:
            print (f"El precio final de su platillo es de ${PRECIO_BASE+10}.")
        elif bebida_postre==2: 
            print (f"El precio final de su platillo es de ${PRECIO_BASE}.")
        
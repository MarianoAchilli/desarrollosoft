# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas las pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print (" 1. No - 2. Si")
pizza=int(input("¿Quiere una pizza vegetariana? "))

if pizza==1:
    print ("Los ingredientes disponibles son: 1. Peperoni, 2. Jamón, 3. Salmón.")
    ingrediente=int(input("Seleccione su ingrediente: "))
    if ingrediente==1:
        print ("Su pizza no es vegetariana y contiene: Mozzarella, tomate y peperoni.")
    elif ingrediente==2:
        print ("Su pizza no es vegetariana y contiene: Mozzarella, tomate y jamón.")
    elif ingrediente==3:
        print ("Su pizza no es vegetariana y contiene: Mozzarella, tomate y jamón.")
else: 
    if pizza==2:
        print ("Los ingredientes disponibles son: 1. Pimiento, 2. Tofu.")
        ingrediente=int(input("Seleccione un ingrediente: "))
        if ingrediente==1:
          print ("Su pizza es vegetariana y contiene: Mozzarella, tomate y pimiento.")
        elif ingrediente==2:
            print ("Su pizza es vegetariana y contiene: Mozzarella, tomate y tofu.")

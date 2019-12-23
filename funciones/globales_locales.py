animal = 'Oso'; #Variable global

def mostrar_animal():
    global animal; #Para cambiar una var global desde la funcion
    animal = 'Ballena' #Ahora animal es una variable local
    print(animal);

mostrar_animal();
print(animal); #Imprime la variable global animal = 'Oso', al usar global animal imprimirá Ballena.
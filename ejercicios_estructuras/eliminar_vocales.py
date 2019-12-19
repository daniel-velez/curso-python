#Eliminar todas las vocales de una frase dado por el usuario y mostrar el nuevo string en pantalla.

vocales = ['a', 'e', 'i', 'o', 'u'];
palabra = str(input("Ingrese una palabra: "));

nuevo_string = '';

for indice in palabra:
    i = 0;
    for vocal in vocales:
        if indice == vocal:
            i += 1;
    if i == 0:
        nuevo_string += indice;

print(nuevo_string);
lista = ["curso", "python", "codi"];
tupla = ("introduccion", "basico", "listas", "tuplas");

nueva_lista = list(tupla); #para crear una lista a partir de la tupla. (la tupla sigue estando igual)

nueva_tupla = tuple(lista); #crear una tupla a partir de la lista sin modificar esta ultima.
print(nueva_lista);
print(nueva_tupla);

#tambien se puede con strings
mensaje = "este es un curso de python";

otra_lista = list(mensaje);
otra_tupla = tuple(mensaje);

print(otra_lista);
print(otra_tupla);
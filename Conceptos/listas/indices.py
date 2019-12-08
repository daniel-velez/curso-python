#Listas

cursos = ["python", "django", "flask", "c", "c++", "c#", "java", "php"];

curso = cursos[0];
#print(curso); -> python

#sublista

sub = cursos[0:3];#-> ["python", "django", "flask"];
print(sub); 

subdos = cursos[:7];#De igual manera inicia desde el primer elemento.
print(subdos);

subtres = cursos[5:];#Empieza desde el quinto elemento.
print(subtres);

subcuatro = cursos[:];#Se copia  toda la lista.
print(subcuatro);

saltos = cursos[1:7:2];#Saltos de 2 en 2.
print(saltos);

inversa = cursos[::-1];#La lista invertida.
print(inversa);

'''
Estas son las formas en las cuales nosotros podemos crear una nueva lista a partir de otra.

    [:] Todos los elementos.
    [start:] Todos los elementos desde el índice establecido(start).
    [:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
    [start:end] Todos los elementos de un rango de índices.
    [start:end:step] Todos los elementos de un rango de índices con saltos.

    De igual forma, este listado es aplicable a las tuplas y los strings.
'''
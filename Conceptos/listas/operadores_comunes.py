lista = [8.17, 90, 1, 5, 44, 1.32];

#Ordenar la lista de forma ascendente
lista.sort();
#Ordenar de forma descendente
lista.sort(reverse=True);
#menor numero
menor = min(lista);
#mayor numero
mayor = max(lista);
#longitud de la lista
longitud = len(lista);
#buscar un elemento
resultado = 1 in lista;
#en que indice esta
indice = lista.index(8.17);
#para saber cuantas veces se repite
contador = lista.count(5);
print(contador);
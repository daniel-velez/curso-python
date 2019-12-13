tupla = (1, 2, 3, 4);

uno = tupla[0];
dos = tupla[1];
tres = tupla[2];
cuatro = tupla[3];

#Lo anterior es lo mismo que:
tupla = (1, 2, 3, 4, 5, 6);
uno, dos, tres, *cuatro = tupla; #asigna a 4 el resto de elementos de la tupla

uno, *dos, cinco, seis = tupla; #asigna a 2 la cantidad necesaria de elementos para que cada variable tenga al menos uno.


#para generar nuevas tuplas:
tupla = (1, 2, 3, 4, 5, 6);
lista = [10, 20, 30, 40];

resultado = zip(tupla, lista); #se crea el objeto de tipo zip
resultado = tuple(resultado); #convertimos a tupla

#se puede agregar más tuplas y más listas
tupla_dos = (100, 200, 300, 400, 500, 600);
resultado = zip(tupla, lista, tupla_dos);
resultado = tuple(resultado);
print(resultado);
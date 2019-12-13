tupla = (10, 20, 30, 40, 50);

#primera forma

primero = tupla[0];
segundo = tupla[1];
ultimo = tupla[-1];

#segunda forma

primer, segundo, _, _, ultimo = tupla; #el 30 y 40 se almacenan en los guiones bajos

#tambien se puede realizar lo siguiente:

primer, segundo, *_, ultimo = tupla;

print(primero);
print(segundo);
print(_);
print(ultimo);
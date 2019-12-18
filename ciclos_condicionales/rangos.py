for valor in range(10): #Se mostrarán lso numeros del 0 al 9
    print(valor);

print("////////////");

for valor in range(1,11): #Se muestran los numeros del 1 al 10
    print(valor);

print("////////////");

for valor in range (1, 10, 2): #Numeros del 1 al 9 con saltos de 2 en 2
    print(valor);

print("////////////");

for valor in "string":
    print(valor);

print("////////////");

lista = [1, 2, 3, 4, 5, 6];

for indice in range( len(lista) ):
    print("indice:", indice, "valor:", lista[indice]);

print("////////////");

for indice, valor in enumerate(lista): #enumerate sirve para recorrer un objeto iterable
    print("indice:", indice, "valor:", valor);
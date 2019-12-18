#Dado una lista de frases ingresadas por el usuario, mostrar en pantalla todas aquellas que sean palíndromo.

numero = int(input("¿Cuántas palabras o frases va a ingresar? "));

lista = [];
i = 0;
lista_invertida = [];
lista_pal = [];

while(len(lista)<numero):
    palabra = str(input("Ingrese la primer palabra: "));
    lista.append(palabra);
    lista_invertida.append(palabra[::-1]);
    if(lista[i] == lista_invertida[i]):
        lista_pal.append(lista[i]);
    i+=1;

print(lista_pal);
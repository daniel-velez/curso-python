#Mostrar en pantalla la frecuencia de aparición de vocales en una frase dada por el usuario.

vocales = ['a', 'e', 'i', 'o', 'u'];

frase = str(input("Ingrese una frase: "));
tamaño = len(frase);
i = 0;
num_vocales = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0};
otro_diccionario = {};

for valor in range(tamaño):
    for vocal in vocales:
        if frase[valor] == vocal:
            num_vocales[vocal] += 1;

for valor in num_vocales:
    if num_vocales.get(valor) != 0:
        print(valor, '=',  num_vocales.get(valor));



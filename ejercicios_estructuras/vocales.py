vocales = ['a', 'e', 'i', 'o', 'u'];

frase = str(input("Ingrese una frase: "));
tamaño = len(frase);
i = 0;

for valor in range(tamaño):
    for vocal in vocales:
        if frase[valor] == vocal:
            i += 1;

print("La frase tiene ", i, " vocales");


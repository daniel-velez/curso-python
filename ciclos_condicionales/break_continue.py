titulo = "Curso de Python3";

for valor in titulo:
    if valor == "P":
        continue;
    print(valor);

print("\n\n////////////////\n\n");

for valor in titulo:
    if valor == "P":
        break;
    print(valor);
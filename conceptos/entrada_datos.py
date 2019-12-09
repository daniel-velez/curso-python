'''
print("¿cuál es tu nombre?");
nombre = input();#Para leer lo que el usuario escriba en consola, entra un string

print("¿Cuál es tu edad?");
edad = int(input());#Para convertir el dato de entrada a entero

print("¿Cuál es tu peso?");
peso = float(input());#Para convertir el dato de entrada a flotante

print("Tienes hambre? (si/no)");
hambriento = input() == "si";
'''
#Otra manera:

nombre = input("¿Cuál es tu nombre?\n");
edad = int(input("¿Cuál es tu edad?\n"));
peso = float(input("¿Cuál es tu peso?\n"));
hambriento = input("¿Estás hambriento? (si/no)\n");

print("Hola", nombre);
print("Edad:", edad);
print("Peso:", peso);
print("Hambriento:", hambriento);
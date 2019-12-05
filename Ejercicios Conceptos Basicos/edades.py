#Mostrar en pantalla True o False si la edad ingresada por dos usuarios es la misma.

edad_uno = int(input("Ingrese la primer edad: "));
edad_dos = int(input("Ingrese la segunda edad: "));

igual = edad_uno is edad_dos;

print(igual);
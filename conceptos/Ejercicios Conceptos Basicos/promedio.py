#Mostrar en pantalla el promedio de un alumno que ha cursado 5 materias (Español, Matemáticas, Economía, Programación, Ingles).

esp = float(input("Ingrese la nota de español: "));
mat = float(input("Ingrese la nota de matematicas: "));
eco = float(input("Ingrese la nota de economia: "));
pro = float(input("Ingrese la nota de programacion: "));
ing = float(input("Ingrese la nota de ingles: "));

promedio = (esp+mat+eco+pro+ing)/5;

print("Es promedio es:", promedio);
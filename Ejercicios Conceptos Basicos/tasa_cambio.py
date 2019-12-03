#Convertir la cantidad de dólares ingresados por un usuario a pesos colombianos y mostrar el resultado en pantalla.

tasa = float(input("¿Cuántos pesos colombianos vale un dolar hoy? "));

dinero = float(input("Ingrese la cantidad de dólares a convertir: "));

total = tasa*dinero;

print(dinero, "equivale a ", total, "pesos colombianos");
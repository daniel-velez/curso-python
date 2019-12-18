#Convertir los grados centígrados ingresados por un usuario a grados Fahrenheit y mostrar el resultado en pantalla.

centigrados = int(input("Ingrese los grados celcius: "));
farenheit = centigrados*1.8+32;
print(centigrados, "°C equivale a ", farenheit, "°F");
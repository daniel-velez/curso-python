#Crear una lista la cual almacene 10 números positivos ingresados por el usuario, mostrar en pantalla: la suma de todos los números, el promedio, el número mayor y el número menor.

lista = [];
suma = 0;
while(len(lista)<10):
    numero = int(input("Ingrese un numero: "));
    lista.append(numero);
    suma += numero; 

mayor = max(lista);
menor = min(lista);
promedio = suma/len(lista);

print(lista);
print("suma total:", suma);
print("promedio:", promedio);
print("numero mayor:", mayor);
print("numero menor:", menor);
    
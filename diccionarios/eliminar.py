diccionario = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g': 7, 'h':8};

del diccionario["a"]; #Para eliminar una llave

valor = diccionario.pop("b"); #Otra forma de eliminar una llave 

diccionario = {}; #Vaciar el diccionario
diccionario.clear(); #Otra forma

print(valor);
print(len(diccionario));
print(diccionario);
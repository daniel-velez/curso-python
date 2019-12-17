diccionario = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g': 7, 'h':8};

resultado = diccionario.keys();#Obtener las llaves del diccionario
#resultado = tuple(resultado);

resultado = diccionario.values();#Obtener los valores del diccionario
#resultado = list(resultado);

resultado = diccionario.items();
resultado = tuple(resultado);
print(resultado);
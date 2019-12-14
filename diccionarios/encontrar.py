diccionario = {"a": 1, "b": 2, "c": 3, "a":4};

resultado = "b" in diccionario; #buscar una llave en el diccionario

resultado = diccionario.get("a"); #retorna el elemento de la llave

resultado = diccionario.setdefault("z", 5); #Obtener el elemento de la llave, en caso de que no este el primer argumento sera la llave y el segundo su elemento
print(resultado);
print(diccionario);
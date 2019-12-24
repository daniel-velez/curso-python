def farenheit(grados):
    return grados * 1.8 + 32;

funcion_aux = farenheit; #Funcion asignada a una variable

#resultado = funcion_aux(32);

#Con lambda
#No hay necesidad de poner el return porque siempre retornan algo
mi_funcion = lambda grados=0: grados * 1.8 + 32;

resultado = mi_funcion(32);
print(resultado);

def farenheit(grados):
    return grados * 1.8 + 32;

funcion_aux = farenheit; #Funcion asignada a una variable

#resultado = funcion_aux(32);

#Con lambda
#No hay necesidad de poner el return porque siempre retornan algo
mi_funcion = lambda grados=0: grados * 1.8 + 32;

resultado = mi_funcion(32);
print(resultado);

#Crear algunas funciones lambdas mas complejas

sin_parametros = lambda : True;

con_valores = lambda val, val1=10, val2=10 : val + val1 + val2;

con_asterisco = lambda *args : args[0];

con_doble_asterisco = lambda **kwargs : args[0];

con_asteriscos = lambda *args , **kwargs : kwargs.get('key', False);
#import calculadora -> ej: calculadora.suma(10, 20);
#from calculadora import * #importamos todas las funciones, ej: suma(10, 20);

from calculadora import (resta, multiplicacion, division);
from calculadora import suma as nueva_suma; #se cambia el nombre de suma

resultado = nueva_suma(10, 20);
print(resultado);

help(nueva_suma); #Para ver la documentación
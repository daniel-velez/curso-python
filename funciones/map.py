
# En Python, la función map nos permite aplicar una función sobre los items de un objeto iterable (lista, tupla, etc...).

# Sintaxis

# map(function, objeto iterable)

# La función retornará un objeto map que posteriormente podemos convertir a una lista o tupla.

def cuadrado(numero):
 return numero * numero

lista = [1,2,3,4,5]
resultado = map(cuadrado, lista)

lista_resultado = list(resultado)
print(lista_resultado)

# Otra forma es con una funcion lambda

lista = [1,2,3,4,5]
resultado = map(lambda numero: numero * numero , lista)

lista_resultado = list(resultado)
print(lista_resultado)


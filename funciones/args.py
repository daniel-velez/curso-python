def suma(*args): #Los parametros ingresados se almacenan en la tupla args
    total = 0;
    print(args); #tupla que contiene los elementos ingresados
    for valor in args:
        total += valor;
    return total;


def usuarios(**kwargs): #Funcion para crear un diccionario con n parametros
    print(kwargs);

resultado = suma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
print(resultado);

usuarios(nombre=True, user=False);

def combinacion(valor_requerido, *args, **kwargs):
    print(valor_requerido); #parametro obligatorio
    print(args); #tupla
    print(kwargs); #diccionario

combinacion("valor_obligatorio", 10, 20, 30, valor=True, ejemplo=False);
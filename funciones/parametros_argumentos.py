def crear_usuario(nombre, apellido, edad): #Funcion que retorma un diccionario
    return {
        'nombre':nombre,
        'apellido':apellido,
        'nombre_completo':"{} {}".format(nombre, apellido),
        'edad':edad
    };

#para colocar un parametro por default es: edad=14 por ejemplo.

usuario = crear_usuario("Daniel", "Velez", 18);

#otra forma
usuario = crear_usuario(apellido = 'Velez', edad=18, nombre='Daniel')

print(usuario["nombre"]);
print(usuario["apellido"]);
print(usuario["edad"]);
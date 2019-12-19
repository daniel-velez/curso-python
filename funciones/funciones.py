def crear_mensaje(nombre):
    mensaje = "Hola {} bienvenido al curso de python3".format(nombre);
    return mensaje;

def suma(v1, v2, v3):
    return v1 + v2+ v3;

def obtener_curso():
    return "Curso de Python", "básico", 3.6;


nuevo = crear_mensaje("daniel");
print(nuevo);

resultado = suma(10, 20, 30);
print(resultado);

curso, nivel, version = obtener_curso();
print(curso, nivel, version);

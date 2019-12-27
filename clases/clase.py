class Usuario:

    def __init__(self, username='', correo='', nombre=''):
        self.username = username;
        self.correo = correo;
        self.nombre = nombre;

    def Saludo(self):
        return "Hola, soy un usuario " + self.nombre;
    
    def mostrar_username(self):
        print(self.username);
    
    def mostrar_correo(self):
        print(self.correo);

pro = Usuario('ejemplo', 'pro@gmail.com', 'pro');
bando = Usuario(correo='bando@yopmail.com');

resultado = pro.Saludo();
print(resultado);

bando.mostrar_correo();

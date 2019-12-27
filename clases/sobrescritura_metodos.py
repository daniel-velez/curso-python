class Animal:
    def comer(self):
        print('Comiendo...');
    
    def dormir(self):
        print('Durmiendo...');

class Mascota:
    def fecha_adopcion(self, fecha):
        self.fecha_de_adopcion = fecha;

class Perro(Animal, Mascota): #Animal se vuelve la clase padre
    def __init__(self, nombre):
        self.nombre = nombre;
    
    def ladrar(self):
        print('Ladrando...');

    def dormir(self):
        print(self.nombre, 'está durmiendo...');
        Animal.dormir(self);
        print('No molestar');

class Gato(Animal, Mascota):
    def ronronear(self):
        print('Ronroneando...');

firulais = Perro('firulais');
firulais.fecha_adopcion('12/11/2018');
print(firulais.fecha_de_adopcion);
firulais.ladrar();
firulais.dormir();


bola_de_nieve = Gato();
bola_de_nieve.comer();

#En caso de que haya un método en común primero se ejecutara el de la clase principal, si no está ese método pasa a buscar a las clases padre.

        

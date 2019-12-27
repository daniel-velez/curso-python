class Animal:
    def comer(self):
        print('Comiendo...');
    
    def dormir(self):
        print('Durmiendo...');

class Perro(Animal): #Animal se vuelve la clase padre
    def __init__(self, nombre):
        self.nombre = nombre;
    
    def ladrar(self):
        print('Ladrando...');

firulais = Perro('firulais');

firulais.comer();
firulais.ladrar();
firulais.dormir();
        

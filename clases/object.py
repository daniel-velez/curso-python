class Gato:
    def __init__(self, nombre):
        self.nombre = nombre;
    
    def __str__(self): #Al no rescribirlo retornará la ubicación en memoria
        return self.nombre;

class Pato(object):
    def __init__(self, nombre):
        self.nombre = nombre;

    def __str__(self): 
        return self.nombre;

gato = Gato('Bigotes');
gato.edad = 6;
pato = Pato('Lucas');

print(gato); #Como se modificó __str__ muestra el nombre
print(pato);                    #>>

print(gato.__dict__);
print(pato.__dict__);



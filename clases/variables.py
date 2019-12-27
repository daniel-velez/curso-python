class circulo:
    pi = 3.14159265; #pi es una variable de clase, todas las instancias la pueden usar

    def __init__(self, radio):
        self.radio = radio; #radio es una variable de instancia

circulo_a = circulo(10);
circulo_b = circulo(20);

circulo_b.radio = 100;

print(circulo_a.radio);
print(circulo_b.radio);


print(circulo_a.pi);
print(circulo_b.pi);
print(circulo.pi);
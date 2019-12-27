class circulo:
    pi = 3.14159265;
    @classmethod #decorador
    def area(cls, radio):
        return cls.pi * radio**2;
    
resultado = circulo.area(10);
print(resultado);
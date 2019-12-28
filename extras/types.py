def saludo(nombre : str) -> None: 
    print("Hola " + nombre);

def suma(num1 : int, num2 : int = 100) -> int:
    return num1 + num2;

saludo('daniel');

resultado = suma(12, 10);
print(resultado);
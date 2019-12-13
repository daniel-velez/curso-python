lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++";

separador = "; ";

resultado = lenguajes.split(separador); #el método split sirve para generar una lista a partir de un string
#print(resultado);

nuevo_string = separador.join(resultado);
#print(nuevo_string);
#print(lenguajes);

texto = '''Este es un texto
con 
saltos 
de 

linea
''';

resultado = texto.splitlines();
print(resultado);
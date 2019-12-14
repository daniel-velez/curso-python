texto = "Curso de Python3";

resultado = texto.capitalize(); #Retorna la string con la primera letra en mayúscula

resultado = texto.swapcase(); #Cambia las minúsculas por mayúsculas y viceversa. 

resultado = texto.upper(); #Todas las letras en mayúscula   

resultado = texto.lower() #todas las letras en minúscula

#Para saber la string está en minúscula o mayúscula
#print(resultado.islower());
#print(resultado.isupper());

resultado = texto.title();

resultado = texto.replace("Python", "ruby"); #Reemplaza la palabra Python por ruby

texto = "Curso de Python3, Python básico";
resultado = texto.replace("Python", "ruby", 1); #Reemplaza una sola vez la palabra python

texto = "  Curso de python3  ";
resultado = texto.strip();
#print(resultado);

curso = "Python";
version = "3";

resultado = "Curso de %s %s" %(curso, version);

resultado = "Curso de {a} {b}".format(b = version, a = curso); #Otra forma
print(resultado);
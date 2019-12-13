curso = "Curso de python3";

caracteres = len(curso); #Para obtener la cantidad de caracteres del string
#print(caracteres);

indice = curso[0]; #Obtener la letra en la posicion 0
#print(indice);

copia = curso[0:16:3]; #Crear un subtring a partir de la variable curso 
print(copia);

#curso[0] = "K"; Retorna un error debido a que los strings son inmutables
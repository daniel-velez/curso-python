mensaje = "Este es un texto muy grande en cuanto a longitud de caracteres se refiere"

resultado = mensaje.count("grande"); #para buscar una palabra o letra en el string

resultado = "texto" in mensaje; #otra manera, pero esta retorna un booleano

resultado = mensaje.find("texto"); #retorna la posicion de la primera letra de la palabra que buscamos.

primero = mensaje.startswith("Est"); #para saber si la palabra ingresada se encuentra al inicio del mensaje

ultimo = mensaje.endswith("ere"); #lo mismo de arriba pero al final.
print(ultimo);
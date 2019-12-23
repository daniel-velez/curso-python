def mi_funcion():
    print("Hello");
    return 100; #Cuando se ejecuta un return sin importar dónde este se termina de ejecutar la funcion
    print("Underworld"); #Esta linea no será ejecutada 
    
#La funcion debe retornar algo para que pueda ser almacenado en una variable, de lo contrario retorna None.
resultado = mi_funcion();
print(resultado);   
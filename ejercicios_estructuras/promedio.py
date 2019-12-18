#Dado un diccionario, el cual almacena las calificaciones de un alumno, siendo las llaves los nombres de las materia y los valores las calificación, mostrar en pantalla el promedio del alumno.

calificaciones = {'calculo':10, 'dibujo':5, 'geografia':9, 'programacion': 11}
total = 0;
num=len(calificaciones);

for valor in calificaciones:
    total += calificaciones.get(valor);
    
total /= num;
print("promedio:", total);


mejor = 0;

for valor in calificaciones:
    
    aux = valor if calificaciones.get(valor)>mejor else aux;
    mejor = calificaciones.get(valor) if calificaciones.get(valor)>mejor else mejor;

print("materia con mejor promedio:", aux);
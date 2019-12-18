#Calcular la cantidad de segundos que le toma a la luz viajar del sol a Marte y mostrar el resultado en pantalla.

distancia_uno = float(input("Digite la distancia (en km) entre el planeta y el sol: "));
distancia_uno_metros = distancia_uno * 1000;
velocidad_luz = 299792458;

tiempo = distancia_uno_metros/velocidad_luz;

print("La luz tarda ", tiempo, "en viajar del sol al planeta");

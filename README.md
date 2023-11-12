# Instalaciones de python necesarias
- pip install customtkinter
- pip install packaging

# Problema 5
 
Implementar un programa que permita colocar un alambre cilíndrico al cual se le puede aplicar una diferencia de potencial (voltaje).

## Parámetros de entrada:
- Largo del alambre.
- Diámetro (debe dar la opción de poderse ingresar el valor en mm o AWG. Si se ingresa el calibre AWG automáticamente mostrar el diámetro en mm).
- Material del que está hecho el conductor: oro, plata, cobre, aluminio o grafito. Para cada uno mostrar el valor de n (densidad de partículas).
- Voltaje aplicado.

## Parámetros de salida:

- Resistencia del alambre.
- Corriente.
- Potencia disipada por el alambre.
- Rapidez de arrastre de los electrones.
- Tiempo que le tomará a los electrones atravesar todo el alambre.

El programa debe mostrar a los electrones moviéndose en la dirección correcta y representar la rapidez de arrastre de manera visual pero no realista (recuerde que estas velocidades son muy pequeñas. Puede multiplicar la velocidad por un factor fijo para que se note la diferencia).

### *Bono: Si se activa una opción, mostrar representativamente los átomos y a un electrón moviéndose de átomo en átomo como una caminata aleatoria (en el código debe implementarse dicha caminata).

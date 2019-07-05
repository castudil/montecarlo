# sumulacion de montecarlo para estimar PI
# descripcion: genera una serie de puntos aleatorios en un cuadrado unitario.
# aquellos puntos que caen dentro del cuarto de circunferencia unitaria son utiles para estimar el valors de PI
# https://www.youtube.com/watch?v=VJTFfIqO4TU
# http://mathfaculty.fullerton.edu/mathews/n2003/montecarlopimod.html
# Autor: Luis Torres, César Astudillo
# Licencia: GPL
# Fecha de Creacion: 1 junio de 2019
# Fecha Ultima acutalizacion: 5 de Julio 2019
# Version  1.0.2

#last updates
# nombres significativos
#comentarios
#encabezado
# validado en mac, windows, ubuntu.


# como instalar pylab
# para mac os es necesartio instalar matplotlib
# https://www.techwalla.com/articles/how-to-install-pylab-on-python
from pylab import *   #para elementos graficos
import random
import math

#paramtetro del sistema
numeroTotalDeIteraciones=10000

circle = plt.Circle((0, 0), 1, color='b', fill=False)  #dibujo de circulo
ax = plt.gca()  # iniciailiza graficos
ax.add_artist(circle) # TODO: averiguar exactamente que hace esta linea
plt.axis([0, 1, 0, 1]) #limites en el grafico

#iteraciones=int(input())


puntosDentroDelCirculo=0 # contador de punto que caen dentro del circulo
for i in range (numeroTotalDeIteraciones):
    puntox=random.random() #se generan los puntos entre 0 y 1
    puntoy=random.random() #se generan los puntos entre 0 y 1
    distanciaDelPuntoAlOrigen=math.sqrt(puntox ** 2 + puntoy ** 2)
    if distanciaDelPuntoAlOrigen <=1: # verficiar si esta dentro de la circunferencia
        puntosDentroDelCirculo= puntosDentroDelCirculo + 1

    plot(puntox, puntoy, 'r*')

aproximacion_pi=4*(puntosDentroDelCirculo / numeroTotalDeIteraciones)
print(aproximacion_pi)
show()
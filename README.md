# simulacion de montecarlo para estimar PI
# descripcion: genera una serie de puntos aleatorios en un cuadrado unitario.
# aquellos puntos que caen dentro del cuarto de circunferencia unitaria son utiles para estimar el valors de PI
# https://www.youtube.com/watch?v=VJTFfIqO4TU
# http://mathfaculty.fullerton.edu/mathews/n2003/montecarlopimod.html
# Autor: Luis Torres, César Astudillo
# Licencia: GPL
# Fecha de Creacion: 1 junio de 2019
# Fecha Ultima acutalizacion: 7 de Julio 2019
# Version  1.0.3

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
vectorPuntosX=[]  #Creacion de vector que guardara cada punto X dentro del ciclo for
vectorPuntosY=[]  #Creacion de vector que guardara cada punto Y dentro del ciclo for
puntosDentroDelCirculo=0 # contador de punto que caen dentro del circulo
for i in range (numeroTotalDeIteraciones):
    puntox=random.random() #se generan los puntos entre 0 y 1
    vectorPuntosX.append(puntox)
    puntoy=random.random() #se generan los puntos entre 0 y 1
    vectorPuntosY.append(puntoy)
    distanciaDelPuntoAlOrigen=math.sqrt(puntox ** 2 + puntoy ** 2)
    if distanciaDelPuntoAlOrigen <=1: # verficiar si esta dentro de la circunferencia
        puntosDentroDelCirculo= puntosDentroDelCirculo + 1

plot(vectorPuntosX, vectorPuntosY, 'r*')

aproximacion_pi=4*(puntosDentroDelCirculo / numeroTotalDeIteraciones)

circle = plt.Circle((0, 0), 1, color='b', fill=False)  #dibujo de circulo
ax = plt.gca()  # iniciailiza graficos
ax.add_artist(circle) # Permite graficar la circunferencia dentro del grafico
plt.axis([0, 1, 0, 1]) #limites en el grafico

print(aproximacion_pi)
show()


#--------------------------------------
#Alumnos:Ivan Castro; Enrique Cerioni. |
#Profesor:Ing. Diego Córdoba.		  |
#Cátedra: Modelos y Simulación.        |
#--------------------------------------
#MONTECARLO<<<

# Librerias
import random, math
import matplotlib.pyplot as plt
import numpy

#clase donde almacenamos los objetos de la lista
class FrecAcum:
    def __init__(self, x, min, max):
        self.x = x
        self.min = min
        self.max = max

def valoresAl():
    media = 0
    varianza = 0
    aux = []
    i = 0
    while i < 100:
        valor = random.uniform(0, 1)
        for x in range(0, len(lista)):
            if (valor >= lista[x].min) and (valor < lista[x].max):
                media += lista[x].x
                aux.append(lista[x].x)
                i += 1
    for x in range(0, len(aux)):
        varianza += math.pow((aux[x] - media / 100), 2)
    media = (media / 100)
    varianza = (varianza / 100)
    print(len(aux))
    print('Datos generados:')
    print(aux)

    plt.title('Muestras obtenidas - Montecarlo')
    plt.hist(aux, 250)
    plt.show()

lista = [FrecAcum(6, 0, 0.008), FrecAcum(7, 0.008, 0.012), FrecAcum(8, 0.012, 0.012), FrecAcum(9, 0.012, 0.016),
     FrecAcum(10, 0.016, 0.024), FrecAcum(11, 0.024, 0.044), FrecAcum(12, 0.044, 0.056), FrecAcum(13, 0.056, 0.064),
     FrecAcum(14, 0.064, 0.084), FrecAcum(15, 0.084, 0.104), FrecAcum(16, 0.104, 0.144), FrecAcum(17, 0.144, 0.176),
     FrecAcum(18, 0.176, 0.228), FrecAcum(19, 0.228, 0.28), FrecAcum(20, 0.28, 0.328), FrecAcum(21, 0.328, 0.38),
     FrecAcum(22, 0.38, 0.436), FrecAcum(23, 0.436, 0.508), FrecAcum(24, 0.508, 0.56), FrecAcum(25, 0.56, 0.612),
     FrecAcum(26, 0.612, 0.652), FrecAcum(27, 0.652, 0.688), FrecAcum(28, 0.688, 0.712), FrecAcum(29, 0.712, 0.744),
     FrecAcum(30, 0.744, 0.788), FrecAcum(31, 0.788, 0.812), FrecAcum(32, 0.812, 0.872), FrecAcum(33, 0.872, 0.896),
     FrecAcum(34, 0.896, 0.912), FrecAcum(35, 0.912, 0.932), FrecAcum(36, 0.932, 0.944), FrecAcum(37, 0.944, 0.964),
     FrecAcum(38, 0.964, 0.972), FrecAcum(39, 0.972, 0.98), FrecAcum(40, 0.98, 0.984), FrecAcum(41, 0.984, 0.984),
     FrecAcum(42, 0.984, 0.988), FrecAcum(43, 0.988, 0.992), FrecAcum(44, 0.992, 0.996), FrecAcum(45, 0.996, 0.996),
     FrecAcum(46, 0.996, 1)]

valoresAl()

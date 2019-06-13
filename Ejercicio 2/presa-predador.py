
#--------------------------------------
#Alumnos:Ivan Castro; Enrique Cerioni. |
#Profesor:Ing. Diego Córdoba.		  |
#Cátedra: Modelos y Simulación.        |
#--------------------------------------
#CASO PRESA-PREDADOR<<<

# Librerias para poder graficar
import matplotlib.pyplot as plt
import numpy

# Condiciones Iniciales
liebres = 500
zorros = 200
capTerreno = 1400
semanas = 1000

tasLie = 0.08
listaLiebres = list(range(semanas))
listaZorros = list(range(semanas))
for i in range(semanas):
    capActual = capTerreno - liebres
    incLiebres = (capActual / capTerreno) * tasLie * liebres
    disZor = 0.2 * zorros
    caza = zorros * liebres
    liebres = liebres + (incLiebres - 0.002 * caza)
    zorros = zorros + (0.0004 * caza - disZor)
    listaLiebres[i] = liebres
    listaZorros[i] = zorros
    print("|N° Semana: ", i, "|Cant. Zorros: ", zorros, "|Cant. liebres: ", liebres)

xTiempo = numpy.linspace(0, semanas, semanas)
yLiebres = numpy.array(listaLiebres)
yZorros = numpy.array(listaZorros)

plt.plot(xTiempo, yLiebres)
plt.plot(xTiempo, yZorros)
plt.show()
plt.plot(yLiebres, yZorros)
plt.show()

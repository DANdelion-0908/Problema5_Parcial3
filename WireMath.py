import math

#Particle density given its molar mass (U) and density (D)
def particleDensity(U: float, D: float):
    # Avogadro's number
    Av = 6.022e23

    return (1/U) * (Av) * (1000) * (D)


#Tansversal area of the wire given its diameter
def transversalArea(d: float):
    return (math.pi * d * d) / 4

#Resistance of the wire given its resistivity (p), length and transversal area
def resistance(p: float, l:float, A: float):
    return (p*l) / A

#Current in the wire given the voltage and the wire resistance
def current(V: float, R: float):
    return  V / R

#Dissipated Power given the voltage and the current through the wire
def dissipatedPower(V: float, I: float):
    return V * I

#Drag speed given the current (I) throught the cable, particle density (n), 
#charge of an electron (q) and the transversal area of the wire (A)
def dragSpeed(I: float, n: float, q: float, A: float):
    return I / (n * q * A)

#Time for the particle to travel the wire given the length of the 
#wire and the drag speed (Vd)
def electronTime(L: float, Vd: float):
    return L / Vd

#Method to correctly show a number with scientific notation 
#(ONLY USE TO SHOW RESULT AND NOT CALCULATE)
def format_to_scientific_notation(number):
    nNumber = format(number, ".2e")
    return nNumber

# #Example data
# Qe = 1.6e-19
# voltge = 250e-3
# largo = 2
# diametro = 2.54e-3

# #El material es plata por ejemplo
# resistividadPlata = 1.47e-8
# masaMolarPlata = 107.87
# densidadPlata = 10.5e3

# #Calculos a realizar en orden
# densidadParticulaN = particleDensity(U= masaMolarPlata, D= densidadPlata)
# print("Densidad de particula: ", format_to_scientific_notation(densidadParticulaN))

# area = transversalArea(d=diametro)

# resistenciaCable = resistance(p= resistividadPlata, l = largo, A= area)
# print("Resistencia: ", format_to_scientific_notation(resistenciaCable))

# corriente = current(V= voltge, R= resistenciaCable)
# print("Corriente: ", format_to_scientific_notation(corriente))

# potencia = dissipatedPower(V= voltge, I= corriente)
# print("Potencia disipada: ", format_to_scientific_notation(potencia))

# velocidad = dragSpeed(I= corriente, n= densidadParticulaN, q= Qe, A= area)
# print("Velocidad de arrastre: ", format_to_scientific_notation(velocidad))

# tiempo = electronTime(L= largo, Vd= velocidad)
# print("Tiempo: ", format_to_scientific_notation(tiempo))

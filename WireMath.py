import math

def particleDensity(U: float, D: float, El: float):

    """
    Particle density given its molar mass (U) and density (D)
    """
    # Avogadro's number
    Av = 6.022e23

    return (1/U) * (Av) * (1000) * (El) * (D)

def transversalArea(d: float):

    """
    Tansversal area of the wire given its diameter
    """
    return (math.pi * d * d) / 4

def resistance(p: float, l:float, A: float):
    """
    Resistance of the wire given its resistivity (p), length and transversal area
    """

    return (p*l) / A

def current(V: float, R: float):

    """
    Current in the wire given the volt age and the wire resistance
    """
    return  V / R

def dissipatedPower(V: float, I: float):

    """
    Dissipated Power given the voltage and the current through the wire
    """
    return V * I

def dragSpeed(I: float, n: float, q: float, A: float):

    """
    Drag speed given the current (I) throught the cable, particle density (n), charge of an electron (q) and the transversal area of the wire (A)
    """
    return I / (n * q * A)

def electronTime(L: float, Vd: float):

    """
    Time for the particle to travel the wire given the length of the wire and the drag speed (Vd)
    """
    return L / Vd

def format_to_scientific_notation(number):

    """
    Method to correctly show a number with scientific notation (ONLY USE TO SHOW RESULT AND NOT CALCULATE)
    """
    nNumber = format(number, ".2e")
    return nNumber

def awg_to_diameter(awg):
    """
    Method that receives the American Wire Gauge (AWG) and returns the diameter of the wire. 
    """
    if(awg == 0):
        diameter = 8.251

    else:
        diameter = 0.127 * (92 ** ((36 - int(awg)) / 39))

    return diameter

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

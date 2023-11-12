from distutils.dist import command_re
from tkinter.font import BOLD
import customtkinter as ctk
import turtle as tr
import tkinter as tk
import Simulation as sim
import WireMath as wm
import MaterialProperties as mp
import RandomWalk as rw

import math
import TurtleAnimation

THEME_COLOR = "#A7D6E3"
CONTRAST_COLOR = "#3A7EBF"

def update_animation():
    # Llamar a la función que actualiza la animación de turtle
    TurtleAnimation.update_animation(jorge)

    # Programar la próxima actualización después de un cierto tiempo (en milisegundos)
    root.after(50, update_animation)  # Actualiza cada 50 milisegundos

def exitProgram():
    root.destroy()

def startSimulation():
    """
    The function "startSimulation" initiates a simulation with specified parameters.
    """
    try:
        if(switch_var.get() == "off"):
            material = materialEntry.get()
            density = mp.properties.get(material)[0]
            weight = mp.properties.get(material)[1]
            resistivity = mp.properties.get(material)[2]
            nElectrons = mp.properties.get(material)[3]
            currentAWG = math.floor(awgEntry.get())
            length = float(widthEntry.get())
            voltage = float(voltageEntry.get())
            particleDensity = wm.particleDensity(weight, density, nElectrons)
            selectedOption = diameterOrAWGSwitch.get()

            tk.messagebox.showinfo(message="Espera hasta que la partícula deje de moverse para cerrar el programa.", title="Recomendación")
            if(selectedOption == 1):
                diameter = wm.awg_to_diameter(currentAWG) / 1000

            elif(selectedOption == 0):
                diameter = float(diameterEntry.get()) / 1000

            area = wm.transversalArea(diameter)
            
            resistance = wm.resistance(resistivity, length, area)
            current = wm.current(voltage, resistance)
            dissipatedPower = wm.dissipatedPower(voltage, current)
            electronSpeed = wm.dragSpeed(current, particleDensity, 1.6e-19, area)
            electronTime = wm.electronTime(length, electronSpeed)

            resistanceLabel.configure(text=f'Resistencia: {wm.format_to_scientific_notation(resistance)} Ω')
            currentLabel.configure(text=f'Corriente: {wm.format_to_scientific_notation(current)} A')
            powerLabel.configure(text=f'Potencia disipada: {wm.format_to_scientific_notation(dissipatedPower)} W')
            speedLabel.configure(text=f'Rapidez de arrastre: {wm.format_to_scientific_notation(electronSpeed)} m/s')
            timeLabel.configure(text=f'Tiempo para finalizar: {wm.format_to_scientific_notation(electronTime)} s')

            if(selectedOption == 0):
                sim.Simulation(gorge, screen, materialEntry.get(), float(diameterEntry.get()) / 2, float(widthEntry.get()))

            elif(selectedOption == 1):
                sim.Simulation(gorge, screen, materialEntry.get(), (diameter / 2) * 1000, float(widthEntry.get()))

        elif(switch_var.get() == "on"):
            tk.messagebox.showinfo(message="Espera hasta que la partícula deje de moverse para cerrar el programa.", title="Recomendación")
            sim.SimulateRandomWalk(screen)

    except:
        tk.messagebox.showerror(message="Asegúrate de llenar todos los campos.", title="¡ERROR!")
            

def setParticleDensity(event):
    """
    The function "setParticleDensity" calculates and displays the particle density in scientific
    notation.
    
    :param event: The `event` parameter is typically used to pass information about the event that
    triggered the function. It can be an object that contains details about the event, such as the
    widget that triggered the event or any additional data associated with the event. In this case, it
    seems like the `event` parameter
    """
    particleDensityCalc = wm.particleDensity(U=mp.properties.get(materialEntry.get())[1], D=mp.properties.get(materialEntry.get())[0], El= mp.properties.get(materialEntry.get())[3])
    particleDensityCalc = wm.format_to_scientific_notation(particleDensityCalc)
    particleDensityLabel.configure(text=f"n: {particleDensityCalc} e/m^3")

def usingAWG():
    """
    The function `usingAWG()` updates the state of two entry fields based on the selected option.
    """
    selectedOption = diameterOrAWGSwitch.get()

    if(selectedOption == 0):
        diameterEntry.configure(state=ctk.NORMAL)
        awgEntry.configure(state=ctk.DISABLED)
    
    elif(selectedOption == 1):
        diameterEntry.configure(state="readonly")
        awgEntry.configure(state=ctk.NORMAL)

def sliderFunction(event):
    """
    The `sliderFunction` function updates the AWG and diameter labels based on the current value of a
    slider.
    
    :param event: The `event` parameter in the `sliderFunction` function is used to capture the event
    that triggered the function. This can be any event, such as a button click or a slider movement,
    depending on how the function is being used. The `event` parameter allows you to access information
    about the
    """
    currentAWG = math.floor(awgEntry.get())
    diameter = wm.awg_to_diameter(currentAWG)

    awgLabel.configure(text=f'AWG: {currentAWG}')
    diameterLabel.configure(text=f'Diámetro: {round(diameter, 4)} mm')

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("Light")

# Main Screen
root = tk.Tk()
root.geometry("1000x720")
root.title("Rapidez de Arrastre de los Electrones")

# Input and Turtle Frame
rootFrame = ctk.CTkScrollableFrame(root, fg_color=THEME_COLOR)
rootFrame.pack(fill=tk.BOTH, expand=1)

frame = tk.Frame(rootFrame, background=THEME_COLOR)

sliderFrame = tk.Frame(frame, width=20, background=CONTRAST_COLOR)

tFrame = ctk.CTkScrollableFrame(rootFrame, width=1300, height=650, orientation="horizontal")

frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=2)
rootFrame.grid_columnconfigure(0, pad=100)

# Creating menu bar
menuBar = tk.Menu()

actionsMenu = tk.Menu(menuBar, tearoff=False)
aboutMenu = tk.Menu(menuBar, tearoff=False)

actionsMenu.add_command(label="Cerrar todo", command=exitProgram)

menuBar.add_cascade(menu=actionsMenu, label="Acciones")
root.config(menu=menuBar)

# Parámetros de entrada

# Longitud del cable
widthEntry = ctk.CTkEntry(frame, placeholder_text="Largo del alambre", width=400, font=("Arial", 15, BOLD))
widthEntry.grid(column=0, row=0)

widthDimension = ctk.CTkLabel(frame, text="m", text_color="white", font=("Arial", 15, BOLD), fg_color=CONTRAST_COLOR, corner_radius=10)
widthDimension.grid(column=1, row=0)

Spacer0 = ctk.CTkLabel(frame, text="").grid(column=0, row=1, pady=15)

# Diámetro del cable
diameterEntry = ctk.CTkEntry(frame, placeholder_text="Diámetro del alambre", width=400, font=("Arial", 15, BOLD))
diameterEntry.grid(column=0, row=2, pady=10)

diameterDimension = ctk.CTkLabel(frame, text="mm", font=("Arial", 15, BOLD), text_color="white",  fg_color=CONTRAST_COLOR, corner_radius=10)
diameterDimension.grid(column=1, row=2)

awgEntry = ctk.CTkSlider(frame, width=350, from_=0, to=40, number_of_steps=41, state=ctk.DISABLED, command=sliderFunction)
awgEntry.grid(column=0, row=4, pady=5)

awgLabel = ctk.CTkLabel(sliderFrame, text="AWG: ", font=("Arial", 15, BOLD), bg_color=CONTRAST_COLOR, text_color="white")
awgLabel.grid(column=0, row=0, sticky=ctk.W, padx=50)

diameterLabel = ctk.CTkLabel(sliderFrame, text='Diámetro: ', font=("Arial", 15, BOLD), bg_color=CONTRAST_COLOR, text_color="white")
diameterLabel.grid(column=1, row=0, sticky=ctk.E)

sliderFrame.grid(column=0, row=5, pady=5)

diameterOrAWGSwitch = ctk.CTkSwitch(frame, text="AWG", command=usingAWG, font=("Arial", 15, BOLD))
diameterOrAWGSwitch.grid(column=0, row=3, pady=5)

Spacer1 = ctk.CTkLabel(frame, text="").grid(column=0, row=6, pady=5)

# Material del cable
materialEntry = ctk.CTkComboBox(frame, values=["Oro", "Plata", "Cobre", "Aluminio", "Grafito"], width=400, command=setParticleDensity, state="readonly", font=("Arial", 15, BOLD))
materialEntry.grid(column=0, row=7)

particleDensityLabel = ctk.CTkLabel(frame, text="n: ",  text_color="white", font=("Arial", 15, BOLD), bg_color=CONTRAST_COLOR, corner_radius=15)
particleDensityLabel.grid(column=0, row=8, ipadx=10, sticky=ctk.W, pady=10, padx=10)

Spacer2 = ctk.CTkLabel(frame, text="").grid(column=0, row=9, pady=5)

# Voltaje aplicado
voltageEntry = ctk.CTkEntry(frame, placeholder_text="Voltaje aplicado", width=400, font=("Arial", 15, BOLD))
voltageEntry.grid(column=0, row=10)

voltageDimension = ctk.CTkLabel(frame, text="V", font=("Arial", 15, BOLD), text_color="white",  fg_color=CONTRAST_COLOR, corner_radius=10)
voltageDimension.grid(column = 1, row=10)

# Submit Button
submitButton = ctk.CTkButton(frame, text="Confirmar", command=startSimulation, height=80, width=300, font=("Arial", 15, BOLD), fg_color="#9C945C", hover_color="#97925e")
submitButton.grid(column=0, row=13)

# Random Switch
switch_var = ctk.StringVar(value="off")
randomButton = ctk.CTkSwitch(frame, text="Caminata Aleatoria", variable=switch_var, onvalue="on", offvalue="off",height=50, width=300, font=("Arial", 15, BOLD))
randomButton.grid(column=0, row=12, pady=25)

frame.grid(column= 0, row=0, rowspan=2)

# Lienzo para Turtle
canvas = tk.Canvas(tFrame, width=3000, height=650)
canvas.grid(column=1, row=0)

tFrame.grid(column=1, row=0, columnspan=4)

screen = tr.TurtleScreen(canvas)

gorge = tr.RawTurtle(screen)

# Output Frame
outputFrame = ctk.CTkScrollableFrame(rootFrame, fg_color=CONTRAST_COLOR, orientation=tk.HORIZONTAL, width=500)
outputFrame.grid(column=2, row=1)

outputFrame.columnconfigure(1, pad=50)
outputFrame.columnconfigure(0, pad=10)
outputFrame.columnconfigure(2, pad=10)
outputFrame.rowconfigure(1, pad=50)

resistanceLabel = ctk.CTkLabel(outputFrame, text="Resistencia: ", text_color="#FFFFFF", font=("Arial", 25, BOLD))
resistanceLabel.grid(column=0, row=0)

currentLabel = ctk.CTkLabel(outputFrame, text="Corriente: ", text_color="#FFFFFF", font=("Arial", 25, BOLD))
currentLabel.grid(column=0, row=1)

columnSpacer = ctk.CTkLabel(outputFrame, text="", font=("Arial", 25))
columnSpacer.grid(column=1)

powerLabel = ctk.CTkLabel(outputFrame, text="Potencia disipada: ", text_color="#FFFFFF", font=("Arial", 25, BOLD))
powerLabel.grid(column=2, row=0)

speedLabel = ctk.CTkLabel(outputFrame, text="Rapidez de arrastre: ", text_color="#FFFFFF", font=("Arial", 25, BOLD))
speedLabel.grid(column=2, row=1)

timeLabel = ctk.CTkLabel(outputFrame, text="Tiempo para finalizar: ", text_color="#FFFFFF", font=("Arial", 25, BOLD))
timeLabel.grid(column=0, columnspan=3, row=2, pady=20)

animationCanvas = tk.Canvas(rootFrame)
animationCanvas.grid(column=3, row=1, pady=20)

animationScreen = tr.TurtleScreen(animationCanvas)
animationScreen.bgcolor("black")
jorge = tr.RawTurtle(animationScreen)

TurtleAnimation.startAnimation(jorge)

update_animation()

root.mainloop()
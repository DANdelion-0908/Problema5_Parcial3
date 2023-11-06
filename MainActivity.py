from tkinter.font import BOLD
import customtkinter as ctk
import turtle as tr
import tkinter as tk
import Simulation as sim
import WireMath as wm
import MaterialProperties as mp

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
        material = materialEntry.get()
        density = mp.properties.get(material)[0]
        weight = mp.properties.get(material)[1]
        resistivity = mp.properties.get(material)[2]
        currentAWG = math.floor(awgEntry.get())
        length = float(widthEntry.get())
        voltage = float(voltageEntry.get())
        particleDensity = wm.particleDensity(weight, density)
        selectedOption = diameterOrAWGSwitch.get()

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

    except:
        tk.messagebox.showerror(message="Asegúrate de llenar todos los campos.", title="¡ERROR!")
            

def setParticleDensity(event):
    particleDensityCalc = wm.particleDensity(U=mp.properties.get(materialEntry.get())[1], D=mp.properties.get(materialEntry.get())[0])
    particleDensityCalc = wm.format_to_scientific_notation(particleDensityCalc)
    particleDensityLabel.configure(text=f"n: {particleDensityCalc} e/m^3")

def usingAWG():
    selectedOption = diameterOrAWGSwitch.get()

    if(selectedOption == 0):
        diameterEntry.configure(state=ctk.NORMAL)
        awgEntry.configure(state=ctk.DISABLED)
    
    elif(selectedOption == 1):
        diameterEntry.configure(state="readonly")
        awgEntry.configure(state=ctk.NORMAL)

def sliderFunction(event):
    currentAWG = math.floor(awgEntry.get())
    diameter = wm.awg_to_diameter(currentAWG)

    awgLabel.configure(text=f'AWG: {currentAWG}')
    diameterLabel.configure(text=f'Diámetro: {round(diameter, 4)} mm')

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("Light")

# Main Screen
root = tk.Tk()
root.configure(bg=THEME_COLOR)
root.title("Rapidez de Arrastre de los Electrones")

#root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1, pad=20)
root.grid_columnconfigure(1,weight=5, pad=20)

# Input and Turtle Frame
frame = tk.Frame(root, background=THEME_COLOR)

sliderFrame = tk.Frame(frame, width=20)

tFrame = ctk.CTkScrollableFrame(root, width=1300, height=500, orientation="horizontal")

frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=2)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, pad=5)

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
widthEntry.grid(column=0, row=0, pady=50)

widthDimension = ctk.CTkLabel(frame, text="m", text_color="white", font=("Arial", 15, BOLD), fg_color=CONTRAST_COLOR, corner_radius=10)
widthDimension.grid(column=1, row=0)

# Diámetro del cable
diameterEntry = ctk.CTkEntry(frame, placeholder_text="Diámetro del alambre", width=400, font=("Arial", 15, BOLD))
diameterEntry.grid(column=0, row=1)

diameterDimension = ctk.CTkLabel(frame, text="mm", font=("Arial", 15, BOLD), text_color="white",  fg_color=CONTRAST_COLOR, corner_radius=10)
diameterDimension.grid(column=1, row=1)

awgEntry = ctk.CTkSlider(frame, width=350, from_=0, to=40, number_of_steps=41, state=ctk.DISABLED, command=sliderFunction)
awgEntry.grid(column=0, row=2, pady=25)

awgLabel = ctk.CTkLabel(sliderFrame, text="AWG: ", font=("Arial", 15, BOLD))
awgLabel.grid(column=0, row=0, sticky=ctk.W, padx=50)

diameterLabel = ctk.CTkLabel(sliderFrame, text='Diámetro: ', font=("Arial", 15, BOLD))
diameterLabel.grid(column=1, row=0, sticky=ctk.E, padx=50)

sliderFrame.grid(column=0, row=3)

diameterOrAWGSwitch = ctk.CTkSwitch(frame, text="AWG", command=usingAWG, font=("Arial", 15, BOLD))
diameterOrAWGSwitch.grid(column=0, row=4, pady=25)

Spacer1 = ctk.CTkLabel(frame, text="").grid(column=0, row=4, pady=5)

# Material del cable
materialEntry = ctk.CTkComboBox(frame, values=["Oro", "Plata", "Cobre", "Aluminio", "Grafito"], width=400, command=setParticleDensity, state="readonly", font=("Arial", 15, BOLD))
materialEntry.grid(column=0, row=5)

particleDensityLabel = ctk.CTkLabel(frame, text="n: ",  text_color="white", font=("Arial", 15, BOLD), bg_color=CONTRAST_COLOR, corner_radius=15)
particleDensityLabel.grid(column=0, row=6, ipadx=10, sticky=ctk.W, pady=10)

Spacer2 = ctk.CTkLabel(frame, text="").grid(column=0, row=7, pady=5)

# Voltaje aplicado
voltageEntry = ctk.CTkEntry(frame, placeholder_text="Voltaje aplicado", width=400, font=("Arial", 15, BOLD))
voltageEntry.grid(column=0, row=8)

voltageDimension = ctk.CTkLabel(frame, text="V", font=("Arial", 15, BOLD), text_color="white",  fg_color=CONTRAST_COLOR, corner_radius=10)
voltageDimension.grid(column = 1, row=8)

frame.grid(column= 0, row=0)

# Submit Button
submitButton = ctk.CTkButton(frame, text="Confirmar", command=startSimulation, height=50, width=300, font=("Arial", 15, BOLD))
submitButton.grid(column=0, row=9, pady=50)

# Lienzo para Turtle
canvas = tk.Canvas(tFrame, width=3000, height=500)
canvas.grid(column=1, row=0)

tFrame.grid(column=1, row=0)

screen = tr.TurtleScreen(canvas)

gorge = tr.RawTurtle(screen)

# Output Frame
outputFrame = ctk.CTkFrame(root, width=400, height=600, fg_color=CONTRAST_COLOR)
outputFrame.grid(column=1, columnspan=2, row=1)

outputFrame.columnconfigure(1, pad=500)
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

animationCanvas = tk.Canvas(root)
animationCanvas.grid(column=0, row=1, pady=20)

animationScreen = tr.TurtleScreen(animationCanvas)
animationScreen.bgcolor("black")
jorge = tr.RawTurtle(animationScreen)

TurtleAnimation.startAnimation(jorge)

update_animation()

root.mainloop()
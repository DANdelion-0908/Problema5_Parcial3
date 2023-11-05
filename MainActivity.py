import customtkinter as ctk
import turtle as tr
import tkinter as tk
import Simulation as sim
import WireMath as wm

def startSimulation():
    """
    The function "startSimulation" initiates a simulation with specified parameters.
    """
    sim.Simulation(gorge, screen, materialEntry.get(), float(diameterEntry.get()) / 2, float(widthEntry.get()))

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("light")

# Main Screen
root = tk.Tk()
root.resizable(False, False)
root.title("Rapidez de Arrastre de los Electrones")

root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=5)

# Input and Turtle Frame
frame = ctk.CTkFrame(root)

tFrame = ctk.CTkScrollableFrame(root, width=1300, height=500, orientation="horizontal")

frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=2)
frame.columnconfigure(0, weight=1)

# Parámetros de entrada
widthEntry = ctk.CTkEntry(frame, placeholder_text="Largo del alambre", width=400)
widthEntry.grid(column=0, row=0, pady=50)

diameterEntry = ctk.CTkEntry(frame, placeholder_text="Diámetro del alambre", width=400) # TODO: Implementar Switch para seleccionar diámetro o AWG
diameterEntry.grid(column=0, row=2)

diameterOrAWTSwitch = ctk.CTkSwitch(frame, text="AWT", onvalue="AWT", offvalue="Diámetro")
diameterOrAWTSwitch.grid(column=0, row=3)

materialEntry = ctk.CTkComboBox(frame, values=["Oro", "Plata", "Cobre", "Aluminio", "Grafito"], width=400)
materialEntry.grid(column=0, row=4, pady=50)

voltageEntry = ctk.CTkEntry(frame, placeholder_text="Voltaje aplicado", width=400)
voltageEntry.grid(column=0, row=5, )

frame.grid(column= 0, row=0, )

# Submit Button
submitButton = ctk.CTkButton(frame, text="Confirmar", command=startSimulation)
submitButton.grid(column=0, row=6, pady=50)

test = ctk.CTkButton(root, text="Hola")
test.grid(column=0, row=1, columnspan=2)

# Lienzo para Turtle
canvas = tk.Canvas(tFrame, width=3000, height=500)
canvas.grid(column=1, row=0)

tFrame.grid(column=1, row=0)

screen = tr.TurtleScreen(canvas)

gorge = tr.RawTurtle(screen)

# Output Frame


root.mainloop()
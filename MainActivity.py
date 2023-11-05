import customtkinter as ctk
import turtle as tr
import tkinter as tk
import Simulation as sim

def startSimulation():
    sim.Simulation(gorge, screen)

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("light")

root = tk.Tk()
root.resizable(False, False)
root.title("Rapidez de Arrastre de los Electrones")

root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=5)

frame = ctk.CTkFrame(root)

frame.grid_rowconfigure(0, weight=1)
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
submitButton.grid(column=0, row=6)

# Lienzo para Turtle
canvas = tk.Canvas(root, width=800, height=650)
canvas.grid(column=1, row=0)

screen = tr.TurtleScreen(canvas)

gorge = tr.RawTurtle(screen)

root.mainloop()
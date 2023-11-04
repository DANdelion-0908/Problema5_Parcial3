import customtkinter as ctk
import turtle as tr
import tkinter as tk

ctk.set_default_color_theme("green")
ctk.set_appearance_mode("light")

root = tk.Tk()
root.geometry("1920x1080")
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
widthEntry.grid(column=0, row=0)

diameterEntry = ctk.CTkEntry(frame, placeholder_text="Diámetro del alambre", width=400) # TODO: Implementar Switch para seleccionar diámetro o AWG
diameterEntry.grid(column=0, row=1, pady=50)

materialEntry = ctk.CTkEntry(frame, placeholder_text="Material del conductor", width=400)
materialEntry.grid(column=0, row=2)

voltageEntry = ctk.CTkEntry(frame, placeholder_text="Voltaje aplicado", width=400)
voltageEntry.grid(column=0, row=3, pady=50)

frame.grid(column= 0, row=0)

canvas = tk.Canvas(root)
canvas.grid(column=1, row=0, sticky=ctk.NSEW)

screen = tr.TurtleScreen(canvas)

testTurtle = tr.RawTurtle(screen)

root.mainloop()
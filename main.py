'''
Imports
'''
import tkinter as tk
import random

##Lista de colores

colores={
    'Rojo':'Red','Azul':'Blue','Verde':'Green',
    'Rosa':'Pink','Negro':'Black','Amarillo':'Yellow','Naranja':'Orange',
    'Blanco':'White','Violeta':'Purple','Marron':'Brown'
}

##Variables globales

timeleft = 30
score = 0

'''
$$$$$$$$$$$$$$$$$$
FUNCIONES$$$$$$$$$
$$$$$$$$$$$$$$$$$$
'''

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft-=1
        timeLabel.config(text = f"Time left: {timeleft}")
        timeLabel.after(1000, countdown)

def start_game(event):
    if timeleft == 30:
        countdown()


#Inicio de ventana
root = tk.Tk()
root.config(width=300,height=300)
root.title("COLORGAME")
#Adornamos y ponemos inputs
etiqueta = tk.Label(text="Escribí el color de las letras. No el color de las palabras:")
etiqueta.place(x=2,y=10)

input = tk.Entry()
input.place(x = 85, y = 250)

##Temporizador
stringTiempo = f'Time left: {timeleft}'
timeLabel = tk.Label(text=stringTiempo)
timeLabel.place(x=110,y=60)

##Eventos
root.bind('<Return>', start_game)

##Mantener en loop la ventana
root.mainloop()



'''
Imports
'''
from cgitb import text
import tkinter as tk
import random as rn

##Lista de colores

colores={
    'rojo':'Red','azul':'Blue','verde':'Green',
    'rosa':'Pink','negro':'Black','amarillo':'Yellow','naranja':'Orange',
    'blanco':'White','violeta':'Purple','marron':'Brown'
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

def cambiar_color():
    global score
    global timeleft

    color_esp = list(colores.keys())
    
    if timeleft>0:
        input.focus_set()
        color_palabra ='rojo'##color_esp[rn.randint(0,len(color_esp)-1)]
        color_letra =colores[color_esp[rn.randint(0,len(color_esp)-1)]]
        labelColor.config(text=color_palabra, fg = color_letra)
        input_value = input.get()
        if(colores[input_value] == color_letra):
            score += 1
        scoreLabel.config(text=f'Puntaje: {score}')
        input.delete(0, tk.END)
        
    

def start_game(event):
    if timeleft == 30:
        countdown()
    cambiar_color()

#Inicio de ventana
root = tk.Tk()
root.config(width=300,height=300)
root.title("COLORGAME")
#Adornamos y ponemos inputs
etiqueta = tk.Label(text="Escribí el color de las letras. No el color de las palabras:")
etiqueta.place(x=2,y=10)

##Label del color
labelColor = tk.Label(root,font = ('Helvetica', 60))
labelColor.place(x=3,y=100)

##INPUT
input = tk.Entry()
input.place(x = 85, y = 250)
input.focus_set()

##Temporizador
stringTiempo = f'Time left: {timeleft}'
timeLabel = tk.Label(text=stringTiempo)
timeLabel.place(x=110,y=60)
##Puntaje
stringPuntaje = f'Puntaje: {score}'
scoreLabel = tk.Label(text=stringPuntaje)
scoreLabel.place(x=110,y=30)



##Eventos(Al apretar enter)
root.bind('<Return>', start_game)

##Mantener en loop la ventana
root.mainloop()



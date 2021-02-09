import tkinter as tk
import random

root = tk.Tk()
hauteur, largeur = 500, 500

canvas = tk.Canvas(root, width=largeur, height=hauteur, bg="black")
canvas.grid()

bouton_recommencer = tk.Button(root, text="Recommencer", bd=3, command=lambda: effacer())
bouton_recommencer.grid()

x0, y0 = 100, 100
x1, y1 = hauteur-100, largeur-100


def couleur(event):
    if couleur_du_rectangle != "blue":
        couleur_du_rectangle = "blue"
    else:
        couleur_du_rectangle = "red"


def effacer():
    couleur_du_rectangle = "red"
canvas.bind('<Button-1>', couleur)
#couleur_du_rectangle = "blue"

rectangle=canvas.create_rectangle(x0, y0, x1, y1, fill=couleur_du_rectangle)



root.mainloop()
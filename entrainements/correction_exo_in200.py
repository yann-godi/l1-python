import tkinter as tk

cpt = 0
continuer = True


def restart():
    global cpt, continuer
    cpt = 0
    continuer = True
    canvas.itemconfigure(rectangle, fill="red")


def est_dans_le_rectangle(x, y):
    """Retourne True si le point de coordonnées {x, y} du canevas est dans le rectangle, et False sinon"""
    return 100 <= x <= 400 and 100 <= y <= 400


def chg_couleur(event):
    global cpt, continuer
    liste_couleur = ["blue", "red"]
    if continuer:
        if est_dans_le_rectangle(event.x, event.y):
            canvas.itemconfigure(rectangle, fill=liste_couleur[cpt])
            cpt = (cpt + 1) % 2
        else:
            continuer = False


racine = tk.Tk()

canvas = tk.Canvas(racine, bg="black", width=500, height=500)
canvas.grid(row=0, column=0)

bouton = tk.Button(racine, text="recomencer", command=restart)
bouton.grid(row=1)

rectangle = canvas.create_rectangle((100, 100), (400, 400), fill="red")

canvas.bind('<Button-1>', chg_couleur)

racine.mainloop()
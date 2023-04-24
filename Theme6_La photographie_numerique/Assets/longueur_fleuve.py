from tkinter import *
from PIL import Image, ImageTk

# Charger l'image
image = Image.open("Loire.jpg")

# Créer une fenêtre
fenetre = Tk()

liste_points=[]

# Créer un canvas avec l'image
canvas = Canvas(fenetre, width=1000, height=1000)
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor=NW, image=image_tk)

def distance(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

# Fonction appelée lorsque l'utilisateur clique sur l'image
def click(event):
    # Obtenir les coordonnées du clic
    x, y = event.x, event.y
    # Obtenir le code RGB du pixel
    couleur = image.getpixel((x, y))
    # Afficher le code RGB
    print("Position du pixel ({}, {}) : couleur {}".format(x, y, couleur))
    
    liste_points.append((x, y))
    distance_sur_fleuve=0
    distance_direct=0
    for i in range(len(liste_points)-1):
        distance_sur_fleuve+=distance(liste_points[i],liste_points[i+1])
    canvas.create_line(liste_points[len(liste_points)-1][0], liste_points[len(liste_points)-1][1], liste_points[len(liste_points)-2][0], liste_points[len(liste_points)-2][1], fill='yellow', width=2)
    distance_direct=distance(liste_points[0],liste_points[len(liste_points)-1])
    if distance_direct>0:
        rapport_distance=distance_sur_fleuve/distance_direct
        print("Rapport des distances: {}".format(rapport_distance))   

# Associer la fonction "click" à l'événement clic de souris
canvas.bind("<Button-1>", click)

# Démarrer la boucle d'événements de la fenêtre
fenetre.mainloop()

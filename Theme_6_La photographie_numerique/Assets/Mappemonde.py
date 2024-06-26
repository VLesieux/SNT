from tkinter import *
from PIL import Image, ImageTk
import random
##############################Définition des variables globales##########################################################################
Frontieres=[

[(333, 133), (324, 128), (320, 112), (331, 103), (344, 109), (342, 118), (342, 125), (341, 130), (333, 131)],

[(489, 195), (506, 159), (533, 188), (534, 206), (515, 247), (502, 225), (490, 195)],

[(597, 356), (652, 324), (675, 346), (688, 380), (673, 400), (655, 412), (639, 394), (616, 390), (595, 402), (600, 353)]

]
########################################################################################
Pays=["France","Inde","Australie"]
Frontiere=[]
pays_a_reperer_indice=0
resultats_corrects=0
###############################la fonction qui interroge###################################
def interroge():
    global Pays
    global pays_a_reperer_indice
    global Frontieres
    global Frontiere
    pays_a_reperer_indice=random.randint(0,len(Pays)-1)
    Frontiere=Frontieres[pays_a_reperer_indice]
    print("Vous devez repérer le pays : ", Pays[pays_a_reperer_indice])
############################################################
# Charger l'image
image = Image.open("Capture_mappemonde.png")
image = image.resize((800, 500))
# Créer une fenêtre
fenetre = Tk()
# Liste des points qui défissent une frontière
liste_points=[]
# Créer un canvas avec l'image
canvas = Canvas(fenetre, width=800, height=500)
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor=NW, image=image_tk)
########################################la fonction qui vérifie si le clic est dans la frontière#####################
def verifie(x,y,liste):    
    calcul=0;
    try:
        for i in range(len(liste)):
            if (i==len(liste)-1):
                yk=(liste[i][1]-(liste[0][1]-liste[i][1])*liste[i][0]/(liste[0][0]-liste[i][0]))/(1-(liste[0][1]-liste[i][1])*(x/y)/(liste[0][0]-liste[i][0]))
                xk=(x/y)*yk
                m=xk/x
                if ((m>=0) and (m<=1)):
                    t=(xk-liste[i][0])/(liste[0][0]-liste[i][0])
                    if ((t>=0) and (t<=1)):
                        calcul+=1
            else:
                yk=(liste[i][1]-(liste[i+1][1]-liste[i][1])*liste[i][0]/(liste[i+1][0]-liste[i][0]))/(1-(liste[i+1][1]-liste[i][1])*(x/y)/(liste[i+1][0]-liste[i][0]))
                xk=(x/y)*yk
                m=xk/x
                if ((m>=0) and (m<=1)):
                    t=(xk-liste[i][0])/(liste[i+1][0]-liste[i][0])
                    if ((t>=0) and (t<=1)):
                        calcul+=1
    except ZeroDivisionError:
        pass
    if (calcul%2==0):
        return False
    else:
        return True
############################################# Fonction appelée lorsque l'utilisateur clique sur l'image############################################
def click(event):
    # Obtenir les coordonnées du clic
    x, y = event.x, event.y
    global Frontiere
    global resultats_corrects
################# Partie à activer pour obtenir une nouvelle frontière #######################
#    liste_points.append((x, y))
#    if len(liste_points)>=2:
#        canvas.create_line(liste_points[len(liste_points)-1][0], liste_points[len(liste_points)-1][1], liste_points[len(liste_points)-2][0], liste_points[len(liste_points)-2][1], fill='red', width=2)    
#    print(liste_points)
###################Partie à commenter pour être interrogé#####################################
    if verifie(x,y,Frontiere):
        del Frontieres[pays_a_reperer_indice]
        del Pays[pays_a_reperer_indice]
        resultats_corrects+=1
        print("Vous avez découvert",resultats_corrects,"pays")
    interroge()
interroge()
###########################Ne pas toucher à cette partie########################################################################
# Associer la fonction "click" à l'événement clic de souris
canvas.bind("<Button-1>", click)
# Démarrer la boucle d'événements de la fenêtre
fenetre.mainloop()
######################################################################################################

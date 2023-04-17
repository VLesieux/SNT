from tkinter import *
from PIL import Image, ImageTk
import random
############################################################
Frontieres=[
[(648, 184), (636, 178), (649, 176), (656, 172), (665, 167), (675, 169), (684, 172), (692, 174), (683, 187), (685, 199), (688, 205), (678, 206), (670, 203), (667, 205), (664, 211), (651, 206), (649, 185)],
[(1010, 248), (1002, 253), (994, 254), (997, 258), (1000, 262), (1002, 268), (999, 275), (997, 280), (991, 288), (985, 292), (981, 296), (987, 302), (988, 305), (983, 309), (978, 313), (982, 320), (988, 326), (994, 328), (996, 323), (1000, 332), (1001, 338), (1004, 347), (1008, 362), (1014, 372), (1018, 384), (1025, 393), (1032, 398), (1034, 392), (1038, 384), (1038, 370), (1040, 362), (1045, 354), (1057, 344), (1063, 332), (1069, 324), (1074, 323), (1074, 314), (1074, 306), (1070, 300), (1064, 300), (1055, 296), (1049, 294), (1038, 292), (1034, 288), (1030, 282), (1032, 275), (1026, 273), (1020, 268), (1018, 264), (1021, 262), (1018, 255), (1010, 247)],
[(1199, 568), (1294, 510), (1318, 537), (1342, 505), (1377, 590), (1321, 657), (1265, 618), (1191, 636), (1194, 567)]]

Pays=["France","Inde","Australie"]
Frontiere=[]

resultats_corrects=0

def interroge():
    global Pays
    pays_a_reperer=random.randint(0,len(Pays)-1)
    global Frontieres
    global Frontiere
    Frontiere=Frontieres[pays_a_reperer]
    print("Vous devez repérer le pays : ", Pays[pays_a_reperer])

interroge()
############################################################
# Charger l'image
image = Image.open("Carte_du_monde_vierge.png")

# Créer une fenêtre
fenetre = Tk()
# Liste des points qui défissent une frontière
liste_points=[]

# Créer un canvas avec l'image
canvas = Canvas(fenetre, width=2000, height=750)
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor=NW, image=image_tk)
#############################################################
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
    global resultats_corrects
    if (calcul%2==0):
        return False
    else:
        resultats_corrects+=1
        print("Vous avez découvert",resultats_corrects,"pays")
        interroge()
    
# Fonction appelée lorsque l'utilisateur clique sur l'image
def click(event):
    # Obtenir les coordonnées du clic
    x, y = event.x, event.y
    global Frontiere
    # Obtenir le code RGB du pixel
#    couleur = image.getpixel((x, y))
    # Afficher le code RGB
#    print("Position du pixel ({}, {}) : couleur {}".format(x, y, couleur))

################# Pour obtenir une nouvelle frontière #######################
#    liste_points.append((x, y))
#    if len(liste_points)>=2:
#        canvas.create_line(liste_points[len(liste_points)-1][0], liste_points[len(liste_points)-1][1], liste_points[len(liste_points)-2][0], liste_points[len(liste_points)-2][1], fill='red', width=2)    
#    print(liste_points)
##############################################################################

    print(verifie(x,y,Frontiere))
 

# Associer la fonction "click" à l'événement clic de souris
canvas.bind("<Button-1>", click)





# Démarrer la boucle d'événements de la fenêtre
fenetre.mainloop()


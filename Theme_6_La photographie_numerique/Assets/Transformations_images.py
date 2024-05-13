import tkinter as tk
from PIL import Image, ImageTk
####################### Noir et Blanc #########################
def noirblanc(image):
    (c,l)=image.size#on récupère ici les dimensions de l’image
    imagearrivee=Image.new('RGB',(c,l))#On crée une image d’arrivée de même dimensions***
    for x in range(c):#On va parcourir toutes les colonnes***
        for y in range(l): #Pour chaque colonne, on va parcourir toutes les lignes***
            pixel=image.getpixel((x,y))#on récupère le triplet (r,g,b)***
            if pixel[0]>127 or pixel[1]>127 or pixel[2]>127 :
                p=(255,255,255)
            else :
                p=(0,0,0)
            imagearrivee.putpixel((x,y),p)
    return imagearrivee
######################### Filtre Bleu ############################
def bleu(image):
    (c,l)=image.size
    imagearrivee=Image.new('RGB',(c,l))
    for x in range(c):
        for y in range(l):
            pixel=image.getpixel((x,y))
            p=(0,0,pixel[2])
            imagearrivee.putpixel((x,y),p)
    return imagearrivee
######################### Filtre Rouge ############################
def rouge(image):
    (c,l)=image.size
    imagearrivee=Image.new('RGB',(c,l))
    for x in range(c):
        for y in range(l):
            pixel=image.getpixel((x,y))
            p=(pixel[0],0,0)
            imagearrivee.putpixel((x,y),p)
    return imagearrivee
######################### Filtre Vert ############################
def vert(image):
    (c,l)=image.size
    imagearrivee=Image.new('RGB',(c,l))
    for x in range(c):
        for y in range(l):
            pixel=image.getpixel((x,y))
            p=(0,pixel[1],0)
            imagearrivee.putpixel((x,y),p)
    return imagearrivee
#########################Transformation nuances de gris############################
def nuance(image):
    (c,l)=image.size
    imagearrivee=Image.new('RGB',(c,l))
    for x in range(c):
        for y in range(l):
            pixel=image.getpixel((x,y))
            moyenne=int((pixel[0]+pixel[1]+pixel[2])/3)
            p=(moyenne,moyenne,moyenne)
            imagearrivee.putpixel((x,y),p)
    return imagearrivee
#########################################################################
# Crée une fenêtre principale
root = tk.Tk()
root.title("Transformations d'image")

# Charge les images et les convertit en format Tkinter
image1 = ImageTk.PhotoImage(Image.open("image.jpg"))

image=Image.open("image.jpg")
(c,l)=image.size#on récupère ici les dimensions de l’image
imagearrivee=Image.new('RGB',(c,l))#On crée une image d’arrivée de même dimensions***
imagearrivee.save("Photo_arrivee.jpg")

photo = ImageTk.PhotoImage(imagearrivee)

# Crée un conteneur pour les images
image_container = tk.Frame(root)
image_container.pack(side=tk.TOP)

# Ajoute les images au conteneur
tk.Label(image_container, image=image1).pack(side=tk.LEFT)

image_label = tk.Label(image_container, image=photo)
image_label.pack(side=tk.LEFT)

# Crée un conteneur pour les boutons
button_container = tk.Frame(root)
button_container.pack(side=tk.BOTTOM)

# Fonction à exécuter lorsqu'on clique sur le premier bouton
def on_button1_click():
    image = Image.open("image.jpg")
    tranformation=noirblanc(image)
    photo = ImageTk.PhotoImage(tranformation)
    image_label.configure(image=photo)
    image_label.image = photo
    Button1.config(bg="grey")

# Fonction à exécuter lorsqu'on clique sur le deuxième bouton
def on_button2_click():
    image = Image.open("image.jpg")
    tranformation=bleu(image)
    photo = ImageTk.PhotoImage(tranformation)
    image_label.configure(image=photo)
    image_label.image = photo
    Button2.config(bg="blue")

# Fonction à exécuter lorsqu'on clique sur le troisième bouton
def on_button3_click():
    image = Image.open("image.jpg")
    tranformation=rouge(image)
    photo = ImageTk.PhotoImage(tranformation)
    image_label.configure(image=photo)
    image_label.image = photo

# Fonction à exécuter lorsqu'on clique sur le quatrième bouton
def on_button4_click():
    image = Image.open("image.jpg")
    tranformation=vert(image)
    photo = ImageTk.PhotoImage(tranformation)
    image_label.configure(image=photo)
    image_label.image = photo
    
# Fonction à exécuter lorsqu'on clique sur le cinquième bouton
def on_button5_click():
    image = Image.open("image.jpg")
    tranformation=nuance(image)
    photo = ImageTk.PhotoImage(tranformation)
    image_label.configure(image=photo)
    image_label.image = photo
    

# Ajoute les boutons au conteneur en leur associant une fonction
Button1=tk.Button(button_container, text="Noir et Blanc", command=on_button1_click).pack(side=tk.LEFT, padx=10)
Button2=tk.Button(button_container, text="Filtre Bleu", command=on_button2_click).pack(side=tk.LEFT, padx=10)
Button3=tk.Button(button_container, text="Filtre Rouge", command=on_button3_click).pack(side=tk.LEFT, padx=10)
Button4=tk.Button(button_container, text="Filtre Vert", command=on_button4_click).pack(side=tk.LEFT, padx=10)
Button5=tk.Button(button_container, text="Nuances de gris", command=on_button5_click).pack(side=tk.LEFT, padx=10)

# Démarre la boucle principale de la fenêtre
root.mainloop()


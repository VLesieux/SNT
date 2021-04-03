from PIL import Image
def new():
    (colonne,ligne)=(200,200)
    imagearrivee=Image.new('RGB',(colonne,ligne))
    for x in range(colonne):
        for y in range(ligne):
            imagearrivee.putpixel((x,y),(0,0,255))
    imagearrivee.save("C:/Users/vincent.lesieuxadmin/Desktop/Photo.JPG")
new()
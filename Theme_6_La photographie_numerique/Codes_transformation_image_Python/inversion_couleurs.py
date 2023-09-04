from PIL import Image
a="C:/Users/vincent.lesieuxadmin/Desktop/Photo_depart.jpg"
im=Image.open(a)
def inversion_couleurs(image):
    (c,l)=image.size
    imagearrivee=Image.new('RGB',(c,l))
    for x in range(c):
        for y in range(l):
            pixel=image.getpixel((x,y))
            p=(255-pixel[0],255-pixel[1],255-pixel[2])
            imagearrivee.putpixel((x,y),p)
    imagearrivee.save("C:/Users/vincent.lesieuxadmin/Desktop/Photo n°2.JPG")
inversion_couleurs(im)
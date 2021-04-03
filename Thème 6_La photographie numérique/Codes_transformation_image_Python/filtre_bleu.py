from PIL import Image
a="C:/Users/vincent.lesieuxadmin/Desktop/Photo_depart.jpg"
im=Image.open(a)
def noirblanc(image):
    (c,l)=image.size
    imagearrivee=Image.new('RGB',(c,l))
    for x in range(c):
        for y in range(l):
            pixel=image.getpixel((x,y))
            p=(0,0,pixel[2])
            imagearrivee.putpixel((x,y),p)
    imagearrivee.save("C:/Users/vincent.lesieuxadmin/Desktop/Bleu.JPG")
noirblanc(im)
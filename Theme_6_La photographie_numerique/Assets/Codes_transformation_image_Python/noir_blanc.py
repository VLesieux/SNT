from PIL import Image
a="C:/Users/vincent.lesieuxadmin/Desktop/Photo_depart.jpg"
im=Image.open(a)
def noir_blanc(image):
    (c,l)=image.size
    imagearrivee=Image.new('RGB',(c,l))
    for x in range(c):
        for y in range(l):
            pixel=image.getpixel((x,y))
            if (pixel[0]>127 or pixel[1]>127 or pixel[2]>127):
                p=(255,255,255)
            else:
                p=(0,0,0)
            imagearrivee.putpixel((x,y),p)
    imagearrivee.save("C:/Users/vincent.lesieuxadmin/Desktop/Photo n°5.JPG")
noir_blanc(im)
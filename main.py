from PIL import Image

try:
    img=Image.open("img.jpg")
except:
    print ("Imagem desabilitada")

size = (812,812)
saved = "Compilado.jpeg"
img=img.convert('L')

img.thumbnail(size)
img.save(saved)
img.show()
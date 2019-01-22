#UNIVERSIDADE FEDERAL DO TOCANTINS
#Trabalho de Processamento de Imagens
#Academicos: Mariana Brito e Vitor Rosa

from PIL import Image
import numpy as np

def negativo(img):

    img_negativa=Image.new('L', (int(img.width), int(img.height)), color = 'white')
    matriz_img_negativa= np.array(img_negativa)
    print ("Matriz da Imagem Nova Negativa branca: ")
    print (matriz_img_negativa)

    M_img_negativa= img_negativa.load()
    M_img=img.load()

    for i in range(0,len(matriz_img)):
        for j in range(0,len(matriz_img)):
		M_img_negativa[i,j]=255-M_img[i,j]

    
    matriz_img_negativa= np.array(img_negativa)
    print ("Matriz da Imagem Nova Negativa Resultante: ")
    print (matriz_img_negativa)
    img_negativa.save('imagem_negativa.jpg')
    img_negativa.show()

def gama(img):

    img_gama=Image.new('L', (int(img.width), int(img.height)), color = 'white')
    matriz_img_gama= np.array(img_gama)
    print ("Matriz da Imagem Nova gama branca: ")
    print (matriz_img_gama)

    M_img_gama= img_gama.load()
    M_img=img.load()
    c=1
    g=1.2
    for i in range(0,len(matriz_img)):
        for j in range(0,len(matriz_img)):
		M_img_gama[i,j]= c * int(pow(M_img[i,j],g))

    
    matriz_img_gama= np.array(img_gama)
    print ("Matriz da Imagem Nova gama Resultante: ")
    print (matriz_img_gama)
    img_gama.save('imagem_gama.jpg')
    img_gama.show()


try:
    img=Image.open("img1.jpg")
except:
    print ("Imagem desabilitada")

size = (1012,1012)
saved = "Compilado.jpeg"
img.show() 
img=img.convert('L') #converter em tons de cinza

img.thumbnail(size) #tamanho a ser impressa
img.save(saved) #salvar com tais paramentros
img.show() #imprimir


matriz_img = np.array(img) #transformar imagem em matriz numerica
print ("Matriz da Imagem cinza: ")

print (matriz_img) #imprimir a matriz

negativo(img)
gama(img)

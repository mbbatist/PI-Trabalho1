#UNIVERSIDADE FEDERAL DO TOCANTINS
#Trabalho de Processamento de Imagens
#Academicos: Mariana Brito e Vitor Rosa


from PIL import Image
import numpy as np

def reducao_vmp(img):

    img_vmp_red=Image.new('L', (int(img.width/2), int(img.height/2)), color = 'white')
    matriz_img_red= np.array(img_vmp_red)
    print ("Matriz da Imagem Nova Reduzida branca: ")
    print (matriz_img_red)
    M_img_vmp_red= img_vmp_red.load()
    M_img=img.load()
    k=0
    l=0

    for i in range(0,len(matriz_img),2):
        for j in range(0,len(matriz_img),2):
            M_img_vmp_red[k,l] = M_img[i,j]
	    l+=1
        l=0
        k+=1
    
    matriz_img_red= np.array(img_vmp_red)
    print ("Matriz da Imagem Nova Reduzida Resultante: ")
    print (matriz_img_red)
    img_vmp_red.save('imagem_reduzida_vmp.jpg')
    img_vmp_red.show()

def ampliacao_vmp(img_reduzida):
    img_vmp_amp=Image.new('L', (int(img_reduzida.width*2), int(img_reduzida.height*2)), color = 'white')
    matriz_img_amp= np.array(img_vmp_amp)
    print ("Matriz da Imagem Nova Ampliada branca: ")
    print (matriz_img_amp)
    M_img_vmp_amp= img_vmp_amp.load()
    M_img=img_reduzida.load()
    k=0
    l=0

    for i in range(0,len(matriz_img),2):
        for j in range(0,len(matriz_img),2):
            M_img_vmp_amp[i,j] = M_img[k,l]
            if (i < img_vmp_amp.height):
                M_img_vmp_amp[i+1,j] =  M_img[k,l]
            if (i < img_vmp_amp.width and j < img_vmp_amp.width):
                M_img_vmp_amp[i+1,j+1] =  M_img[k,l]
            if (j < img_vmp_amp.width):
                M_img_vmp_amp[i,j+1] =  M_img[k,l]
	    l+=1
        l=0
        k+=1

    matriz_img_amp= np.array(img_vmp_amp)
    print ("Matriz da Imagem Nova Ampliada Ampliada: ")
    print (matriz_img_amp)
    img_vmp_amp.save('imagem_ampliada_vmp.jpg')
    img_vmp_amp.show()


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

reducao_vmp(img)
img_reduzida=Image.open("imagem_reduzida_vmp.jpg")
ampliacao_vmp(img_reduzida)


	
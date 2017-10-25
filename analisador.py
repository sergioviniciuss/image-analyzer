import scipy as sp
from scipy.misc import imread
from scipy.signal.signaltools import correlate2d as c2d
import math
from VideoCapture import Device
import time
import os #http://pydoc.org/1.6/os.html
import shutil
import Image

cam = Device()

os.mkdir('IA') #cria pasta IA

#funcao que captura as imagens da webcam usando a biblioteca VideoCapture
for i in range(1,16):
    if i==1:
            tiraFoto = raw_input("pressione enter para tirar a foto base")
            cam.saveSnapshot('im%s.jpg' %i) #tira a foto e arquiva
            shutil.move("im%s.jpg" %i, "IA") #move im3 para IA, removendo de onde estava
            print "\n \n foto base arquivada"    
    else:
         tiraFoto = raw_input("pressione enter para tirar a foto %s" %i) #apenas para o usuario ter controle do momento que vai tirar as fotos
         cam.saveSnapshot('im%s.jpg' %i) #tira a foto e arquiva
         shutil.move("im%s.jpg" %i, "IA") #move im3 para IA, removendo de onde estava
         print "\n \n foto %s arquivada" %i 
         if i==15:
                  print " A correlacao de pearson esta sendo calculada..."   




#for i in range(1,16): #funcao que pega as imagens da webcam
	#cam.saveSnapshot('im%s.jpg' % i)
	#shutil.move("im%s.jpg" % i, "IA") #move im3 para IA, removendo da onde estava
	#qualquerCoisa = raw_input("pressione a tecla pra tirar foto")
	#time.sleep(1)
	#print "\n \n a proxima foto sera tirada em 2 segundos"
	#time.sleep(1)
	#print "a foto %s sera tirada em 1 segundo" %i
	#time.sleep(1)


def get(i):
    # get JPG image as Scipy array, RGB (3 layer)
    data = imread('im%s.jpg' % i)
    # convert to grey-scale using W3C luminance calc
    data = sp.inner(data, [299, 587, 114]) / 1000.0
    # normalize per http://en.wikipedia.org/wiki/Cross-correlation
    cross =(data - data.mean()) / data.std() #calcula a correlacao cruzada
    return cross


x= 1
vet =[]
for im in os.listdir("IA"): #percorre as imagens no diretorio IA
	os.chdir("IA") #sobe um diretorio para achar a imagem
	im = get (x) #faz um get pra cada imagem
	vet.append(im) #joga num vetor para poder manipular dps
	x = x+1	
	os.chdir ("..") #desce um diretorio para poder funcionar o for :P
time.sleep(2)
print " Tenha paciencia..."
numimage = 0
pearson =[]
for i in vet[0]: #calcula da imagem principal, que no caso seria a primeira
	x = (i-vet[0].mean())
	y = math.sqrt (sum(pow(i-vet[0].mean(),2)))	
for i in vet: #para cada elemento do vetor, ou seja, para cada imagem
	for j in i:  #para cada pixel dessa imagem
		w = (j-i.mean())
		t = math.sqrt (sum(pow(j-i.mean(),2)))
	z = sum(x*w)/(y*t) #calcula o z com a imagem principal
	numimage = numimage + 1
	pearson.append((z,"im%s.jpg" % numimage) ) #adiciona numa nova lista
	
print "\n\n A paciencia eh a maior de todas as virtudes"
time.sleep(5)
print "\n\n em poucos segundo o resultado sera exibido.."

for i in range(3,0,-1):
    time.sleep(1)
    print (i)

pearson.sort()
pearson.reverse()

os.chdir("IA")
os.mkdir('pasta1')
os.mkdir('pasta2')
os.mkdir('pasta3')


arquivo = open("index.html", "w")
arquivo.write("<html><head><title>Trabalho Final de IA</title></head><body>\n")

arquivo.write('<h1>Imagens com similaridade <b>alta</b></h1>\n')

for i in range(1,6):
    shutil.move(pearson[i-1][1], "pasta1")
    arquivo.write('<h2>Imagem <i>' + pearson[i-1][1] + '</i> ('+str(pearson[i-1][0])+'):</h2><br />\n')
    arquivo.write('<a href=pasta1/"' + pearson[i-1][1] + '"><img border=0 src="pasta1/' + pearson[i-1][1] + '" height=240 width=320 /></a><br />\n')
    
arquivo.write('<h1>Imagens com similaridade <b>media</b></h1>')	

for i in range(6,11):
    shutil.move(pearson[i-1][1], "pasta2")
    arquivo.write('<h2>Imagem <i>' + pearson[i-1][1] + '</i> ('+str(pearson[i-1][0])+'):</h2><br />\n')
    arquivo.write('<a href=pasta2"' + pearson[i-1][1] + '"><img border=0 src="pasta2/' + pearson[i-1][1] + '" height=240 width=320 /></a><br />\n')
	
arquivo.write('<h1>Imagens com similaridade <b>baixa</b></h1>\n')

for i in range(11,16):
    shutil.move(pearson[i-1][1], "pasta3")
    arquivo.write('<h2>Imagem <i>' + pearson[i-1][1] + '</i> ('+str(pearson[i-1][0])+'):</h2><br />\n')
    arquivo.write('<a href=pasta3"' + pearson[i-1][1] + '"><img border=0 src="pasta3/' + pearson[i-1][1] + '" height=240 width=320 /></a><br />\n')

arquivo.write('</body></html>')

arquivo.close()		
print "Resultado de Pearson em ordem decrescente:", pearson
quit()

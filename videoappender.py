#esse script vai ser usado para encontrar arquivos wav no diretorio "textolido"
#e depois vai jogar em uma lista chamda "tempos" o tempo de cada audio
#e depois vai jogar em uma lista chamada "escrita" tudo o que estiver escrito em "textoprincipal.txt"
#logo após, ele pegará cada frase de "textoprincipal.txt" e irá puxar imagens do diretorio "simple_images"
#sempre ignorando a primeira e segunda imagem de cada subdiretorio e colocando as imagens restantes em posições aleatórias dentro da imagem "background/background.png"
#esse problema de ignorar a primeira e segunda imagem de cima eu resolvi no proprio script de image downloader
#troquei o a imagem background por uma imagem que eu criei
#após adicionar as imagens de forma aleatória, ele vai criar uma imagem nova com o nome "imagemfinal_X.png" onde X é o número da imagem na pasta "edited_images"
#e o número é contado em uma variavel chamada "contador"
#após tudo isso ele vai pegar as imagens da pasta "edited_images" e vai colocar em um video com o nome "videofinal.mp4" com o formato de vídeo mp4
#cada imagem vai ser adicionada pelo tempo de cada audio da  lista "tempos" e o som vai ser adicionado em cada imagem
#e depois vai jogar o video no diretorio "videos"

#copilot, qual lib que eu uso para converter o video?
#devo usar o ffmpeg?
#https://www.ffmpeg.org/
#ou o ffmpeg-python? como eu baixo e instalo?
#
#https://www.ffmpeg.org/ffmpeg-formats.html

from gettext import find
import os
import glob
from posixpath import split
import ffmpeg
import pathlib
import re
from PIL import Image
import random
import subprocess
import shutil

currentpath = pathlib.Path(__file__).parent.resolve()
the_images_path = r"C:\Users\pentaedro\Documents\testedownload\estranho\enverio\simple_images"

#variaveis globais
#criando uma lista para armazenar o tempo de cada audio
#criando um contador
#criando uma lista para armazenar o texto
tempos = []
contador = 0
escrita = []
valid_images_formats = ['.jpg', '.png', '.ico', '.gif', '.jpeg']
Image.MAX_IMAGE_PIXELS = None

#pega o texto do arquivo "textoprincipal.txt"
f = open("textoprincipal.txt", 'r')



#essa função vai pegar o tempo de cada audio e jogar em uma lista chamada "tempos"
def findwav():
    #global
    global tempos
    temp = []
    #pega todos os arquivos wav no diretorio "textolido"
    for file in glob.glob("textolido/*.wav"):
        #pega o nome do arquivo
        nome = os.path.basename(file)
        #pega o tempo do arquivo
        tempo = ffmpeg.probe(file)['format']['duration']
        #joga o tempo no final da lista
        tempos.append(nome+tempo)
        #printa o nome e o tempo
        #print(nome, tempo)
    #ordena a lista de acordo com o nome do arquivo
    for x in sorted_nicely(tempos):
        x = re.sub(r'^.*?wav', '', x)
        temp.append(x)
        #print(x)
    #joga a lista ordenada em "tempos"
    tempos = temp
    #printa a lista
    #print(tempos)

#eu roubei de https://stackoverflow.com/questions/2669059/how-to-sort-alpha-numeric-set-in-python
def sorted_nicely( l ): 
    """ Sort the given iterable in the way that humans expect.""" 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)



findwav()


#essa função vai pegar o texto de "textoprincipal.txt" e jogar em uma lista chamada "escrita"
def findtext():
    #global
    global escrita
    #criando um loop em que enquanto ler uma palavra do texto, vai jogar no dicionario
    #e vai printar tudo que estiver dentro do arquivo de texto já separado em silabas
    #por ultimo esta adicionando a um arquivo de texto par uso futuro
    for wordfinded in f:
    #check if its a link
        if wordfinded.startswith("https"):
            #important to remove the last character of the string
            wut = len(wordfinded)
            #important to remove all the characters 
            wut2 = wut - 1
            #remove all the characters
            if wut2 != wut:
                wordfinded = wordfinded.replace(wordfinded[wut2], "")
                wut2 =- 1
            else:
                pass
            continue
        #security check to make sure that the string will not blow windows
        else:
            wordfinded = wordfinded.replace("<", "")
            wordfinded = wordfinded.replace(">", "")
            wordfinded = wordfinded.replace(":", "")
            wordfinded = wordfinded.replace("\"", "")
            wordfinded = wordfinded.replace("/", "")
            wordfinded = wordfinded.replace("|", "")
            wordfinded = wordfinded.replace("?", "")
            wordfinded = wordfinded.replace("*", "")
            wordfinded = wordfinded.replace("\\", "")
            wordfinded = wordfinded.replace("//", "")
            wordfinded = wordfinded.replace('"', "")
            wordfinded = wordfinded.replace("\n", "")
            #usei apenas para debug
            #print(wordfinded)
            #apenas para não dar erro que nem no caso do image downloader que fudeu tudo antes
            for splitwordfinded in wordfinded.split(","):
                if splitwordfinded.startswith(" "):
                    splitwordfinded = splitwordfinded.replace(" ", "_")
                    splitwordfinded = splitwordfinded.strip("_")
                    splitwordfinded = splitwordfinded.replace("_", " ")
                    splitwordfinded = splitwordfinded.strip()
                    escrita.append(splitwordfinded)
                else:
                    splitwordfinded = splitwordfinded.strip()
                    escrita.append(splitwordfinded)
            #debugcount = 0
            #for x in escrita:
            #    print(tempos[debugcount], x)
            #    debugcount += 1


findtext()

#essa função vai pegar o texto da lista "escrita" e puxar as imagens do diretorio "simple_images"
#e jogar em cima de uma imagem base chamada "background.png" na pasta "background"
#e depois jogar o video no diretorio "edited_images"
def makeimg():
    global the_images_path
    global valid_images_formats
    global escrita
    global tempos
    countbase = 0
    temposcount = 1
    savepath = r"C:\Users\pentaedro\Documents\testedownload\estranho\enverio\edited_images"
    os.mkdir(savepath) 
    #encontra as imagens na lista "escrita"
    for words in escrita:
        backgroundimage = Image.new("RGBA", (3840,2160), "#00FF00FF")
        print(f"estamos em: \n{words}")
        #prepara o diretorio para salvar as imagens
        forpath = words.replace(" ", "_")
        #pega todos os formatos validos
        for valid_formats in valid_images_formats:
            #pega as imagens
            for file in glob.glob(os.path.join(the_images_path, forpath, f"*{valid_formats}")):
                #pega o arquiv
                im = Image.open(file)
                #altera o tamanho da imagem para ela não ficar grande demais
                size = random.randint(1152, 1536), random.randint(648, 864)
                im.thumbnail(size, Image.Resampling.LANCZOS)
                #esse é uma passo extra experimental para reduzir a quantidade de imagens sobrepostas
                #usei uma formula para tentar achar os valores que me agradassem
                #temprs = round(float(tempos[temposcount]), 6)
                #rs = random.randint(0, int(temprs*10000))
                #na formula acima encontrei
                #33443 37623 18892 38887 14900
                #entao arredondei para baixo o menor e para cima o maior
                rs = random.randint(14000, 39000)
                #print(rs)
                random.seed(rs)
                #joga a imagem no background só que evitando dela ir para fora do mesmo
                randomX = random.randint(0, abs(3840 - im.width))
                randomY = random.randint(0, abs(2160 - im.height))
                #esse base 0 é importante para começar o processo
                if countbase == 0:
                    editim = backgroundimage
                    editim.paste(im, (randomX, randomY))
                    tempsave = os.path.join(savepath, f"imagem_final_{temposcount}")
                    editim.save(f"{tempsave}.png", "PNG")
                    countbase += 1
                #esse segundo apenas manteve o processo, mas sem definir um background, trazendo a imagem anterior colada
                elif 1 <= countbase <= 3:
                    editim.paste(im, (randomX, randomY))
                    tempsave = os.path.join(savepath, f"imagem_final_{temposcount}")
                    editim.save(f"{tempsave}.png", "PNG")
                    countbase += 1
                #esse valor deve ser alterado toda vez que altera a quantidade de imagens, sendo o valor determinado por (imagens pesquisadas -1)
                elif countbase == 4:
                    editim.paste(im, (randomX, randomY))
                    tempsave = os.path.join(savepath, f"imagem_final_{temposcount}")
                    editim.save(f"{tempsave}.png", "PNG")
                    countbase = 0
                    temposcount += 1
    else:
        print("essa parte está pronta")
                


makeimg()


#aqui irei fazer o video pegando o tempo dos audio colocando as imagens nesse tempos e colocando no video
#ao mesmo tempo irei colocar os audios em ordem correta
#após todo o processo salvo tudo em um video só usando ffmpeg
def merge_all():
    #globais
    global escrita
    global tempos
    #variaveis
    contagemdetempos = 1
    final_image_path = r"C:\Users\pentaedro\Documents\testedownload\estranho\enverio\edited_images"
    final_audio_path = r"C:\Users\pentaedro\Documents\testedownload\estranho\enverio\textolido"
    #eu usei a lista de tempos para definir o loop principal da função
    for x in tempos:
        #arrendondando
        x = round(float(x), 2)
        #abrindo os diretorios e escrevendo e fechando
        w = open("essascoisas.txt", 'a')
        m = open("audiolocations.txt", 'a')
        w.write(f"file '{final_image_path}\imagem_final_{contagemdetempos}.png'\nduration {x}\n")
        m.write(f"file '{final_audio_path}\linha{contagemdetempos}.wav'\n")
        w.close()
        m.close()
        #usei apenas para debbugar
        #w = open("essascoisas.txt", 'r')
        #print(w.read())
        #w.close()
        contagemdetempos += 1
    else:
        #após o loop principal, ele termina com 1 a mais na contagem, voltamos isso para uma pequena correção que tenho que fazer no meu ffmpeg
        #alguns não precisam, mas no fim é apenas uma parte sem audio
        #contagemdetempos -= 1
        #debug
        #w = open("essascoisas.txt", 'a')
        #w.write(f"file '{final_image_path}\imagem_final_{contagemdetempos}.png'")
        #w.close()
        #w = open("essascoisas.txt", 'r')
        #print(w.read())
        #w.close()
        #desativei o modo seguro por conta do windows e caminhos absolutos
        #usei cfr por conta que vfr estava dando alguns erros de compatibilidade
        subprocess.call('ffmpeg -f concat -safe 0 -i essascoisas.txt -vsync cfr -pix_fmt yuv420p output.mp4', shell=True)
        subprocess.call('ffmpeg -f concat -safe 0 -i audiolocations.txt -vsync cfr -pix_fmt yuv420p output.wav', shell=True)
        subprocess.call('ffmpeg -i output.mp4 -i output.wav -c:v copy -c:a aac final_output.mp4', shell=True)
        shutil.move(r"C:\Users\pentaedro\Documents\testedownload\estranho\enverio\final_output.mp4", r"C:\Users\pentaedro\Documents\testedownload\estranho\enverio\video\final_output.mp4")
    
        

merge_all()


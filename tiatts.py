# Python program to show
# how to convert text to speech
import pyttsx3
import os
import pathlib

currentpath = pathlib.Path(__file__).parent.resolve()
newpath = "textolido"
path = os.path.join(currentpath, newpath)


try: 
    os.mkdir(path) 
except OSError as error: 
    print("already exists")

# Initialize the converter
converter = pyttsx3.init()

# Set properties before adding
# Things to word
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_ptBR_DanielM"
  
# Use male voice
converter.setProperty('voice', voice_id)

  
# Sets speed percent 
# Can be more than 100
converter.setProperty('rate', 150)
# Set volume 0-1
converter.setProperty('volume', 1)
  
# Queue the entered text 
# There will be a pause between
# each one like a pause in 
# a sentence

#criando uma variavel para ler de um texto
f = open("textoprincipal.txt", 'r')

print (path)
num = 1
#criando um loop em que enquanto ler uma palavra do texto, vai jogar no dicionario
#e vai printar tudo que estiver dentro do arquivo de texto já separado em silabas
#por ultimo esta adicionando a um arquivo de texto par uso futuro
for word in f:
    #check if its a link
    if word.startswith("https"):
        #important to remove the last character of the string
        wut = len(word)
        #important to remove all the characters 
        wut2 = wut - 1
        #remove all the characters
        if wut2 != wut:
            word = word.replace(word[wut2], "")
            wut2 =- 1
        else:
            pass
        continue
    #separate the string everytime there is a , in a for loop
    else:
        for word in word.split(","):
            converter.say(word)
            converter.save_to_file(word, f'{path}\linha{num}.wav')
            num +=1
  
            # Empties the say() queue
            # Program will not continue
            # until all speech is done talking
  
            converter.runAndWait()
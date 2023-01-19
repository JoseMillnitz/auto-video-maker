from simple_image_download import simple_image_download as simp
import os
import pathlib
import re

#preparations
response = simp.simple_image_download
f = open("textoprincipal.txt", 'r')
currentpath = pathlib.Path(__file__).parent.resolve()

for say in f:
    #check if its a link
    if say.startswith("https"):
        #important to remove the last character of the string
        wut = len(say)
        #important to remove all the characters 
        wut2 = wut - 1
        #remove all the characters
        if wut2 != wut:
            say = say.replace(say[wut2], "")
            wut2 =- 1
        else:
            pass
        continue
    #security check to make sure that the string will not blow windows
    else:
        say = say.replace("<", "")
        say = say.replace(">", "")
        say = say.replace(":", "")
        say = say.replace("\"", "")
        say = say.replace("/", "")
        say = say.replace("|", "")
        say = say.replace("?", "")
        say = say.replace("*", "")
        say = say.replace("\\", "")
        say = say.replace("//", "")
        say = say.replace('"', "")
        response().download(say, 8)
        #print(say)
        #i dont know why but i had to add this to make it work, its not a good idea to use this, but i dont know how to fix it except for this way
        #thank you windows for doing things hard
        
        #this next one is because its annoying me how some accents of other languages (like portuguese) are being replaced by variations of "ã"


        #and also google for the next part
        #i want delete the first and second downloaded image
        #i want to split the string everytime there is a , in a for loop
        for word in say.split(","):
            #i want to remove spaces and make it _
            if word.startswith(" "):
                #generate a ok wordpath for that parts where it starts with a space
                wordpath = word.replace(" ", "_")
                wordpath = wordpath.strip("_")
                wordpath = wordpath.strip()
                #generate a ok word
                #there was bug where the output is n/{word}\n
                #solved, there was no n/ to start with, it was a problem with the wordpath variable
                #so striped the wordpath variable and it worked in the newword variable
                newword = re.sub(r'_', ' ', wordpath)
                os.remove(f"{currentpath}/simple_images/{wordpath}/{newword}_1.png")
                os.remove(f"{currentpath}/simple_images/{wordpath}/{newword}_2.png")
                os.remove(f"{currentpath}/simple_images/{wordpath}/{newword}_3.png")
            else:
                word = word.strip()
                word1 = word.replace(" ", "_")
                os.remove(f"{currentpath}/simple_images/{word1}/{word}_1.png")
                os.remove(f"{currentpath}/simple_images/{word1}/{word}_2.png")
                os.remove(f"{currentpath}/simple_images/{word1}/{word}_3.png")

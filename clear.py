import os
import pathlib
import shutil

currentpath = pathlib.Path(__file__).parent.resolve()

try:
    shutil.rmtree(f"{currentpath}/edited_images")
    print("acabei de remover as imagens editadas")
except:
    print("já removido imagens editadas")
    pass
try:
    shutil.rmtree(f"{currentpath}/textolido")
    print("acabei de remover a leitura")
except:
    print("já removido leitura")
    pass
try:
    shutil.rmtree(f"{currentpath}/simple_images")
    print("acabei de remover as imagens baixadas")
except:
    print("já removido imagens baixadas")
    pass
try:
    os.remove(f"{currentpath}/output.mp4")
    print("acabei de remover as imagens juntas")
except:
    print("já removido imagens juntas")
    pass
try:
    os.remove(f"{currentpath}/output.wav")
    print("acabei de remover os audios juntos")
except:
    print("já removido audios juntos")
    pass
try:
    os.remove(f"{currentpath}/essascoisas.txt")
    print("acabei de remover a lista de imagens")
except:
    print("já removido lista de imagens")
    pass
try:
    os.remove(f"{currentpath}/audiolocations.txt")
    print("acabei de remover a lista de audios")
except:
    print("já removido lista de audios")
    pass
#importando bibliotecas
import pyphen

#importando dicionario em portugues brasileiro
dic = pyphen.Pyphen(lang='pt_BR')

#criando uma variavel para ler de um texto
f = open("textoprincipal.txt", 'r')
#variavel para escrever em um arquivo depois
outputtxt = open("OUTPUT.txt", "w")

#criando um loop em que enquanto ler uma palavra do texto, vai jogar no dicionario
#e vai printar tudo que estiver dentro do arquivo de texto já separado em silabas
#por ultimo esta adicionando a um arquivo de texto par uso futuro
for word in f:
    awoo = dic.inserted(word)
    print(awoo)
    outputtxt.write(awoo)
    outputtxt.close()
print("")
input("de enter para sair")

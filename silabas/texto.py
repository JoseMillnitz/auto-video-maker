#importando bibliotecas
import pyphen

#importando dicionario em portugues brasileiro
dic = pyphen.Pyphen(lang='pt_BR')

#criando uma variavel para ler de um texto
f = open("textoprincipal.txt", 'r')

#criando um loop em que enquanto ler uma palavra do texto, vai jogar no dicionario
#e vai printar tudo que estiver dentro do arquivo de texto já separado em silabas
for word in f:
    awoo = dic.inserted(word)
    print(awoo)

print("")
input("de enter para sair")

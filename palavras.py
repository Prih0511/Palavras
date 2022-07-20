#conte quantas palavras há no arquivo. ok
print("-" *20)

filename = "palavras.txt"
palavras = []

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open (filename, "r", encoding="utf-8") as f:
#with open abre e fecha sozinho o arquivo.
    for line in f:
        palavras.append(line.lower())
print ("Temos", len(palavras), "palavras no arquivo.")


print("-" *20)

#conte quantas vezes cada letra do alfabeto aparece no arquivo. ok
def cada_letra_no_arquivo (alfabeto, palavras):
    
    unica_palavra = ""
    unica_palavra = unica_palavra.join(palavras).lower()
#join juntou tudo em uma unica frase e dai ele conta tudo sem pular linha.
    for letra in alfabeto:
        print(f"letra \"{letra}\" : {unica_palavra.count(letra)}")
        #print(unica_palavra.count("a"))


print("-" *20)

#conte quantas palavras começam com cada letra do alfabeto. ok
def cada_letra_começa (alfabeto, palavras):
    """esperado uma lista de alfabeto e uma lista de palavras"""
    contador = 0
    for letra in alfabeto:
        for palavra in palavras:
            if palavra[0] == letra:
                contador = contador +1
        print (f"{letra} palavras começao: {contador}")


print("-" *20)               

#identifique as palavras que começam com a mesma 3 letras do seu nome. salva separado



#identifique as palavras que possuem todas as letras do seu nome. salva separado
#identifique todas as palavras que sao palindromos . salva separado

#cada_letra_no_arquivo(alfabeto, palavras)
#cada_letra_começa(alfabeto, palavras)
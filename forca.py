import random


def jogar():
    print("**********************************************")
    print("**********BEM VINDO AO JOGO DA FORCA**********")
    print("**********************************************")

    # define-se as variáveis de regra do jogo: Enforcou = Perdeu | Acertou = Ganhou,
    # Enquanto não acertar e/ou ganhar: continuar a jogar
    # Abaixo teremos a palavra secreta

    # Para escolher a palavra o programa terá que ler o arquivo txt com algumas palavras
    # É preciso usar uma lista para guardar as palavras
    # Também precisa limpar as strings

    # O programa tem q aceitar letra minuscula e maiscula e apenas letras:
    #  - Para isso é preciso tratar a entrada, usei a função lower()
    #  - Para saber se é uma letra, usei isaplha()


    #with abre o arquivo e fecha, mesmo que dê erro
    with open("palavras.txt") as arquivo:

        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)


    # será usado um random para sortear a palavra
    # cada palavra terá um index, por esse, saberemos qual será a palavra escolhida

    numero_da_palavra = random.randrange(0,len(palavras))

    palavra_secreta = palavras[numero_da_palavra].lower()

    # A função len() me diz o tamanho da string
    quantidade_letras = len(palavra_secreta)
    letras_acertadas = ["_"] * quantidade_letras

    acertou = False
    enforcou = False
    tentativas = 0

    while (not acertou and not enforcou):
        print("Escolha uma letra")
        print("A palavra têm {} letras".format(quantidade_letras))
        print(" ".join(letras_acertadas))
        chute = input("Digite uma letra:")

        if (chute.isalpha()):
            chute = chute.lower()
        else:
            print("Você deve digitar apenas letras")
        if(chute in palavra_secreta):
            index = 0
            print("Você acertou! Tem a letra {}".format(chute))
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1
            print("Você errou! Restam {} tentativas".format(6-tentativas))
        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
            print("Parabéns! Você acertou a palavra")
    else:
            print("Você perdeu")

if (__name__ == "__main__"):
    jogar()

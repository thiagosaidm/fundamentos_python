# define-se as variáveis de regra do jogo: Enforcou = Perdeu | Acertou = Ganhou,
# Enquanto não acertar e/ou ganhar: continuar a jogar
# Abaixo teremos a palavra secreta

# Para escolher a palavra o programa terá que ler o arquivo txt com algumas palavras
# É preciso usar uma lista para guardar as palavras
# Também precisa limpar as strings

# O programa tem q aceitar letra minuscula e maiscula e apenas letras:
#  - Para isso é preciso tratar a entrada, usei a função lower()
#  - Para saber se é uma letra, usei isaplha()

import random

def jogar():

    imprime_boasvindas()
    palavra_secreta = carregar_palavra()

    quantidade_letras = len(palavra_secreta) # A função len() me diz o tamanho da string
    letras_acertadas = ["_"] * quantidade_letras

    acertou = False
    enforcou = False
    tentativas = 0

    while (not acertou and not enforcou):

        print("A palavra têm {} letras".format(quantidade_letras))
        print(" ".join(letras_acertadas))

        chute = pede_chute()

        if(chute in palavra_secreta):
            marcar_letra_acertada(chute, letras_acertadas, palavra_secreta)
        else:
            tentativas += 1
            mostrar_erro(tentativas)
            desenha_forca(tentativas)

        enforcou = tentativas == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
            mostrar_mensagem_ganhou()
    else:
            mostrar_mensagem_perdeu(palavra_secreta)

def imprime_boasvindas():
        print("**********************************************")
        print("**********BEM VINDO AO JOGO DA FORCA**********")
        print("**********************************************")

def carregar_palavra():

        with open("palavras.txt") as arquivo:  # with abre o arquivo e fecha, mesmo que dê erro
            palavras = []

            for linha in arquivo:
                linha = linha.strip()
                palavras.append(linha)

            numero_da_palavra = random.randrange(0, len(palavras))  # será usado um random para sortear a palavra

            palavra_secreta = palavras[numero_da_palavra].lower()  # cada palavra terá um index, por esse, saberemos qual será a palavra escolhida

            return palavra_secreta

def pede_chute():
    chute = input("Digite uma letra:")
    if (chute.isalpha()):
        chute = chute.lower()
    else:
        print("Você deve digitar apenas letras")
    return chute

def marcar_letra_acertada(chute, letras_acertadas, palavra_secreta):
    index = 0
    print("Você acertou! Tem a letra {}".format(chute))
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def mostrar_erro(tentativas):
    print("Você errou! Restam {} tentativas".format(6 - tentativas))

def mostrar_mensagem_ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mostrar_mensagem_perdeu(palavra_secreta):
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogar()


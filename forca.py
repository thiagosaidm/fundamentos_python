import random


def jogar():
    print("**********************************************")
    print("**********BEM VINDO AO JOGO DA FORCA**********")
    print("**********************************************")

    # define-se as variáveis de regra do jogo: Enforcou = Perdeu | Acertou = Ganhou,
    # Enquanto não acertar e/ou ganhar: continuar a jogar
    # Abaixo teremos a palavra secreta

    # O programa tem q aceitar letra minuscula e maiscula e apenas letras:
    #  - Para isso é preciso tratar a entrada, usei a função lower()
    #  - Para saber se é uma letra, usei isaplha()

    palavra_secreta = "Python"
    palavra_secreta = palavra_secreta.lower()
    # A função len() me diz o tamanho da string
    quantidade_letras = len(palavra_secreta)
    letras_acertadas = ["_"] * quantidade_letras

    acertou = False
    enforcou = False
    tentativas = 0

    while (not acertou and not enforcou):
        print("Jogando")
        print("A palavra têm {} letras".format(quantidade_letras))
        print(" ".join(letras_acertadas))
        chute = input("Digite uma letra:")

        if (chute.isalpha()):
            chute = chute.lower()
        else:
            print("Você deve digitar apenas letras")
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1
        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if(acertou):
            print("Parabéns! Você acertou a palavra")
        else:
            print("Você perdeu")

if (__name__ == "__main__"):
    jogar()

import random
def jogar():

    print("**********************************************")
    print("**********BEM VINDO AO JOGO DA FORCA**********")
    print("**********************************************")

    #define-se as variáveis de regra do jogo: Enforcou = Perdeu | Acertou = Ganhou,
    #Enquanto não acertar e/ou ganhar: continuar a jogar
    # Abaixo teremos a palavra secreta

    # O programa tem q aceitar letra minuscula e maiscula e apenas letras:
    #  - Para isso é preciso tratar a entrada, usei a função lower()
    #  - Para saber se é uma letra, usei isaplha()

    palavra_secreta = "Python"
    palavra_secreta = palavra_secreta.lower()
    #A função len() me diz o tamanho da string
    quantidade_letras = len(palavra_secreta)

    acertou = False
    enforcou = False

    while(not acertou and not enforcou):
        print("Jogando")
        print("A palavra têm {} letras".format(quantidade_letras))
        chute = input("Digite uma letra:")
        if(chute.isalpha()):
            chute = chute.lower()
        else:
            print("Você deve digitar apenas letras")

        index = 0

        for letra in palavra_secreta:
            index = index + 1
            if(chute == letra):
                print("Têm a {} na posição {}". format(letra, index))



if (__name__ == "__main__"):
    jogar()
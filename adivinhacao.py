import random


def jogar():

    imprime_boas_vindas()

    pontuacao_total = 0

    while True:
        pontos = 0

        iniciar_jogo = input("****PRESSIONE ->1<- PARA INICIAR****   ")

        if (iniciar_jogo == '1'):

            print("****VAMOS COMEÇAR O JOGO****")
            print("Selecione a dificuldade")

            dificuldade = int(input("Fácil (1) // Médio(2) // Dífícil (3):"))

            if (dificuldade == 1):
                total_tentativas = 10
            elif (dificuldade == 2):
                total_tentativas = 5
            else:
                total_tentativas = 3

            print("DICA: ESCOLHA UM NÚMERO DE 1 A 10")
            break
        else:
            print("DIGITE ->1<- PARA COMEÇAR")

    numero_secreto = random.randint(1, 10)

    tentativa = 1

    while (tentativa <= total_tentativas):
        numero_usuario = int(input("Digite um número: "))

        print("tentativa {} de {}".format(tentativa, total_tentativas))

        if (numero_usuario < 1 or numero_usuario > 10):
            print("O número deve estar entre 1 e 10")
            continue

        if (numero_secreto == numero_usuario):
            print("PARABÉNS, VOCÊ ACERTOU")
            pontos = 10
            pontuacao_total += pontos
            print("Você fez {} pontos".format(pontos))
            break
        elif (numero_secreto > numero_usuario):
            print("CHUTE BAIXO")
        else:
            print("CHUTE ALTO")

        tentativa = tentativa + 1

        if (total_tentativas < tentativa):
            print("você escolheu o número:{}".format(numero_usuario))
            print("O NUMERO ERA:{}".format(numero_secreto))
            print("Você fez {} pontos".format(pontos))
            print("******GAME OVER******")

    while True:
        escolha_input = input("***** APERTE -> 0 PARA SAIR || APERTE ->1 PARA TENTAR NOVAMENTE ")

        if (escolha_input == '0'):
            print("Você fez {} pontos no total".format(pontuacao_total))
            print("SAIU DO JOGO")
            break
        elif (escolha_input == '1'):
            print("*************NOVA RODADA*******************")
            print("Selecione a dificuldade")

            dificuldade = int(input("Fácil (1) // Médio(2) // Dífícil (3):"))
            total_tentativas = 0

            if (dificuldade == 1):
                total_tentativas = 10
            elif (dificuldade == 2):
                total_tentativas = 5
            else:
                total_tentativas = 3

            numero_secreto = random.randint(1, 10)

            tentativa = 1

            while (tentativa <= total_tentativas):
                numero_usuario = int(input("Digite um número: "))
                print("tentativa {} de {}".format(tentativa, total_tentativas))

                if (numero_secreto == numero_usuario):
                    print("PARABÉNS, VOCÊ ACERTOU")
                    print("O NUMERO ERA:{}".format(numero_secreto))
                    pontuacao_total += pontos
                    print("Você fez {} pontos".format(pontuacao_total))
                    break
                elif (numero_secreto > numero_usuario):
                    print("CHUTE BAIXO")
                else:
                    print("CHUTE ALTO")

                tentativa = tentativa + 1

                if (total_tentativas < tentativa):
                    print("você escolheu o número:{}".format(numero_usuario))
                    print("O NUMERO ERA:{}".format(numero_secreto))
                    print("Você fez {} pontos no total".format(pontuacao_total))
                    print("******GAME OVER******")


        else:
            print("ESCOLHA UMA OPÇÃO VÁLIDA(0 OU 1)")

def imprime_boas_vindas():
    print("********************************")
    print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
    print("********************************")

if (__name__ == "__main__"):
    jogar()

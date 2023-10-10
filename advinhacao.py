import random

print("********************************")
print("BEM VINDE AO JOGO DE ADVINHAÇÃO")
print("********************************")

while True:
    iniciar_jogo = input("****PRESSIONE ->1<- PARA INICIAR****   ")

    if (iniciar_jogo == '1'):
        print("****VAMOS COMEÇAR O JOGO****")
        print("DICA: ESCOLHA UM NÚMERO DE 1 A 10")
        print("VOCÊ TEM 3 CHANCES")
        break
    else:
        print("DIGITE ->1<- PARA COMEÇAR")


numero_secreto = random.randint(1,10)

total_tentativas = 3
tentativa = 1



while(tentativa <= total_tentativas):
    entrada = input("Digite um número: ")
    numero_usuario = int(entrada)
    print(tentativa, "de", total_tentativas)
    print("você escolheu o número:", numero_usuario)

    if (numero_secreto == numero_usuario):
        print("PARABÉNS, VOCÊ ACERTOU")
    elif (numero_secreto > numero_usuario):
        print("CHUTE BAIXO")
    else:
        print("CHUTE ALTO")

    if (tentativa == 2):
        print("Ultima chance, escolha com sabedoria")
    elif(tentativa == 3):
        print("O NUMERO ERA:", numero_secreto)
        print("******GAME OVER******")

    tentativa = tentativa + 1

while True:
    escolha_input = input("***** APERTE -> 0 PARA SAIR || APERTE ->1 PARA TENTAR NOVAMENTE ")

    if(escolha_input == '0'):
        print("SAIU DO JOGO")
        break
    elif(escolha_input == '1'):
        print("********************************")
        print("bem vindo ao jogo de adivinhação")
        print("********************************")

        numero_secreto = random.randint(1,10)

        total_tentativas = 3
        tentativa = 1

        while (tentativa <= total_tentativas):
            entrada = input("Digite um número: ")
            numero_usuario = int(entrada)
            print(tentativa, "de", total_tentativas)
            print("você escolheu o número:", numero_usuario)

            if (numero_secreto == numero_usuario):
                print("PARABÉNS, VOCÊ ACERTOU O NUMERO")
            elif (numero_secreto > numero_usuario):
                print("CHUTE BAIXO")
            else:
                print("CHUTE ALTO")

            if (tentativa == 2):
                print("Ultima chance, escolha com sabedoria")
            elif (tentativa == 3):
                print("O NUMERO ERA:",numero_secreto)
                print("******GAME OVER******")

            tentativa = tentativa + 1
    else:
        print("ESCOLHA UMA OPÇÃO VÁLIDA(0 OU 1)")










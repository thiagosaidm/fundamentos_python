print("********************************")
print("bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 42

entrada = input("Digite um número: ")
numero_usuario = int(entrada)


print("você escolheu o número:", numero_usuario)

if (numero_secreto == numero_usuario):
    print("Você acertou")
elif (numero_secreto > numero_usuario):
    print("chute baixo")
else:
    print("chute alto")

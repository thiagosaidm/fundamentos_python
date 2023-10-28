
#Classes e Objetos

class Conta:
    def __init__(self, num, titular, saldo, limite): #init é o mesmo que o constructor
        self.__num = num # usa-se self para fazer referencia a atributos e metodos da classe
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        print("Conta Criada {}". format(titular))
    def extrato(self):
            print("O saldo do titular {}, é de {}". format(self.__titular, self.__saldo))
            print("Limite cheque especial é de {}". format(self.__limite))

    def depositar(self):
        valor_deposito = int(input("Digite o valor a ser depositado"))
        print("O valor de R${} foi depositado em conta". format(valor_deposito))
        self.__saldo += valor_deposito

    def sacar(self):
        valor_saque = int(input("Digite o valor a ser sacado"))
        if(valor_saque <= self.__saldo):
            self.__saldo -= valor_saque
            print("Você sacou R${} da sua conta". format(valor_saque))
        else:
            print("Você não tem saldo suficiente para essa operação, seu saldo é de R${}". format(self.__saldo))
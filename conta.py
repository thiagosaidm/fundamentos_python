
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

    def depositar(self, valor):
        print("O valor de R${} foi depositado em conta do titular {}". format(valor, self.__titular))
        self.__saldo += valor

    def sacar(self, valor):
        if(valor <= self.__saldo):
            self.__saldo -= valor
            print("Você sacou R${} da sua conta". format(valor))
        else:
            print("Você não tem saldo suficiente para essa operação, seu saldo é de R${}". format(self.__saldo))

    def transferir(self, valor, destino):
            if(valor <= self.__saldo):
                self.sacar(valor)
                print("Você transferiu R${}".format(valor))
                destino.depositar(valor)
            elif(valor >= self.__saldo):
                print("Você não tem saldo suficiente para essa operação, seu saldo é de R${}".format(self.__saldo))



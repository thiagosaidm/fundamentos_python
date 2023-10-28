
#Classes e Objetos

class Conta:
    def __init__(self, num, titular, saldo, limite): #init é o mesmo que o constructor
        self.num = num # usa-se self para fazer referencia a atributos e metodos da classe
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        print("Conta Criada {}". format(titular))
    def extrato(self):
            print("O saldo do titular {}, é de {}". format(self.titular, self.saldo))
            print("Limite cheque especial é de {}". format(self.limite))

    def depositar(self):
        valor_deposito = int(input("Digite o valor a ser depositado"))
        print("O valor de R${} foi depositado em conta". format(valor_deposito))
        self.saldo += valor_deposito

    def sacar(self):
        valor_saque = int(input("Digite o valor a ser sacado"))
        if(valor_saque <= self.saldo):
            self.saldo -= valor_saque
            print("Você sacou R${} da sua conta". format(valor_saque))
        else:
            print("Você não tem saldo suficiente para essa operação, seu saldo é de R${}". format(self.saldo))
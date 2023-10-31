
#Classes e Objetos

class Conta:
    def __init__(self, num, titular, saldo, cheque, limite): #init é o mesmo que o constructor
        self.__num = num # usa-se self para fazer referencia a atributos e metodos da classe
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__cheque = cheque
        print("Conta Criada {}". format(titular))

    # Static Method : é um metodo que pode ser chamado direto da classe
    # Não necessita da instancia de uma classe para ser chamado, eu posso chamar o "codigo_banco" sem criar um objeto
    @staticmethod
    def codigo_banco():
        return "33394"

    def extrato(self):
            print("O saldo do titular {}, é de {}". format(self.__titular, self.__saldo))
            print("Limite cheque especial é de {}". format(self.__limite))

    def depositar(self, valor):
        print("O valor de R${} foi depositado em conta do titular {}". format(valor, self.__titular))
        self.__saldo += valor

    def autorizador_movimentacao(self, valor_saque):
        valor_disponivel = self.__saldo + self.__cheque
        return valor_saque <= valor_disponivel


    def sacar(self, valor):
        if(self.autorizador_movimentacao(valor)):
            self.__saldo -= valor
            print("Você sacou R${} da sua conta". format(valor))
        else:
            print("Você não tem saldo suficiente para essa operação, seu saldo é de R${}". format(self.__saldo))

    def transferir(self, valor, destino):
            if(valor <= self.autorizador_movimentacao(valor)):
                self.sacar(valor)
                print("Você transferiu R${}".format(valor))
                destino.depositar(valor)
            elif(valor >= self.__saldo + self.__cheque):
                print("Você não tem saldo suficiente para essa operação, seu saldo é de R${}".format(self.__saldo))


    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

    #property
    # é usado para definir métodos especiais (métodos de propriedades)
    # controlam o acesso, atribuição e deleção de atributos de maneira mais flexível

    @property # o decorador marca o acesso pelo getter
    def cheque(self):
        print("Usando property")
        return self.__cheque

    @cheque.setter  # o decorador marca o metódo setter @nome_atributo.setter
    def cheque(self, cheque):
        self.__cheque = cheque
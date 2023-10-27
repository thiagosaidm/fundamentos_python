
#Classes e Objetos


class Conta:
    def __int__(self, num_conta , titular, saldo, limite): #init é o mesmo que o constructor
        self.num_conta = num_conta # usa-se self para fazer referencia a atributos e metodos da classe
        self.titutlar = titular
        self.saldo = saldo
        self.limite = limite
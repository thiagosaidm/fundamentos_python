
#Classes e Objetos


class Conta:
    def __init__(self, num, titular, saldo, limite): #init é o mesmo que o constructor
        self.num = num # usa-se self para fazer referencia a atributos e metodos da classe
        self.titutlar = titular
        self.saldo = saldo
        self.limite = limite
        print("Conta Criada {}". format(titular))

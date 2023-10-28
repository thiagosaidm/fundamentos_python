
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formata_data(self):
        print("0{}/0{}/{}". format(self.dia, self.mes, self.ano))




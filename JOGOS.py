import forca
import adivinhacao

print("********************************")
print("********BEM VINDO(A)************")
print("********************************")

print("*ADIVINHAÇÃO (>1<)*")
print("*FORCA (>2<)*")

selecionaJogo = int(input("SELECIONE UM JOGO:   "))


if(selecionaJogo == 1):
    print("........INICIANDO JOGO DA ADIVINHAÇÃO.......")
    adivinhacao.jogar_adivinhacao()
elif(selecionaJogo == 2):
    print("........INICIANDO JOGO DA FORCA.......")
    forca.jogar_forca()
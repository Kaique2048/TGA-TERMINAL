import msvcrt
from time import sleep

#IMPORTANDO FUNCOES QUE IRA USAR
from estoque import ESTOQUE
from vendas import vender
from vendedo import cad_vend


while True:
    print('\n________________\033[92m【T】【G】【A】\033[0m____________________')


    print("\nＣＡＤＡＳＴＲＡＲ ＶＥＮＤＥＤＯＲ\n" \
    "\nＶＥＮＤＡＳ\n" \
    "\nＥＳＴＯＱＵＥ\n")

    print("Selecione: ", end="", flush=True)

    #FUNCAO AUTOMATIZADA DE ESCOLHA
    selecao = msvcrt.getche().decode()

    print('\n' * 2)


    if selecao == "1":
        sleep(1)
        cad_vend()

    elif selecao == "2":
        sleep(1)
        vender()

    elif selecao == "3":
        sleep(1)
        ESTOQUE()


    #RETORNAR PARA O MENU INICIAL
    elif selecao == "s":
        sleep(2)
        break





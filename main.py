import msvcrt
from time import sleep

#IMPORTANDO FUNCOES QUE IRA USAR
from sistema_estoque.estoque import ESTOQUE
from sistema_vendas.login import vender
from sistema_cadastro.vendedo import cad_vend
from utills.escrever import escrever


while True:
    escrever("\n\033[95m        ＢＥＭ　ＶＩＮＤＯ    \033[0m\n", 0.1)

    sleep(1)
    print("\033[92m\nＩＮＩＣＩＡＮＤＯ ＣＯＤＩＧＯ...\033[0m\n", )
    sleep(3)
    print("\n\033[91mＲ Ｅ Ｃ Ａ Ｄ Ｏ\033[0m: \033[91mSE CASO QUEIRA VOLTAR PRO COMEÇO PRESSIONE [s] E ESPERE, NAO APERTE MAIS NADA ALEM DE [s], NEM ENTER\033[0m")
    sleep(2)    
    print("\n\033[1;94mＳＩＳＴＥＭＡ ＤＥ ＶＥＮＤＥＤＯＲＥＳ\033[0m\n" \
        "\n\033[1;94mＶＥＮＤＡＳ\033[0m\n" \
        "\n\033[1;94mＥＳＴＯＱＵＥ\033[0m\n\n")
    
    print("\033[31mSelecione\033[0m: ", end="", flush=True)

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





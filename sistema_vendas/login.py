import json
import msvcrt
from time import sleep

from sistema_vendas.ped_vend import pedido_venda
from sistema_vendas.orcamento import orcar

def vender():


    with open('dados/cadastro.json', 'r', encoding="utf-8") as arquivo:
        vendedores = json.load(arquivo)

    try:
        codigo = int(input("CODIGO DE VENDEDOR: "))
    except ValueError:
        print("\n\033[91mPOR FAVOR COLOQUE O CODIGO DO VENDEDOR\033[0m")
        return
    

    vendedor_encontrado = False

    for vendedor in vendedores["vendedores"]:
        if vendedor["CODIGO"] == codigo:
            print(f"\n Vendedor: {vendedor["NOME"]}")
            print(f" Codigo: {vendedor["CODIGO"]}")


            vendedor_encontrado = True
            break

    if not vendedor_encontrado:
        print("\n\033[31mVENDEDOR NÃO ENCONTRADO\033[0m")
        return

    while True:
        sleep(2)
        print("\n=========VENDAS========\n")

        print('[1] PEDIDO DE VENDA\n' \
        '[2] ORCAMENTO\n')

        selecao = msvcrt.getche().decode()

        if selecao == "1":
            pedido_venda(vendedor)

        elif selecao == "2":
            orcar()

        elif selecao == "s": 
            return





        
        




    
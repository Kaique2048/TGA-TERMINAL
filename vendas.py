import json
import msvcrt
from time import sleep

from vendido import pedido_venda

def vender():


    with open('cadastro.json', 'r', encoding="utf-8") as arquivo:
        vendedores = json.load(arquivo)

    codigo = int(input("CODIGO DE VENDEDOR: "))

    vendedor_encontrado= False

    for vendedor in vendedores["vendedores"]:
        if vendedor["CODIGO"] == codigo:
            print(f"\n Vendedor: {vendedor["NOME"]}")
            print(f" Codigo: {vendedor["CODIGO"]}")


            vendedor_encontrado = True
            break

    if not vendedor_encontrado:
        print("Vendendor não encontrado")
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
            print('')

        elif selecao == "s": 
            return





        
        




    
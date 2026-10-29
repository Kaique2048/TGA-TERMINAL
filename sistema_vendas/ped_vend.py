from time import sleep
import json
from utills.reais import reais


def pedido_venda(vendedor):

    with open("dados/estoque.json", "r", encoding="utf-8") as arquivo:
        estoque = json.load(arquivo)

    """CARRINHO DE MATERIAIS DE COMPRA"""
    itens = []


    cliente = input("\n\n\033[92mNOME\033[0m:").upper()

    if cliente == "":
            cliente = "CONSUMIDOR"
            print("\n\033[91mNAO DEIXE DE COLOCAR O NOME\033[0m\n")
    else:
        print()


    print("=" * 30)
    print("[01]: DINHEIRO\n" \
        "[02]:   PIX\n" \
        "[03]: BOLETO X1")
    print("=" * 30)
    form_pag = input("\n\033[92mFORMA DE PAGAMENTO\033[0m: ")

    if form_pag == "01":
        form_pag = "DINHEIRO"
    elif form_pag == "02":
        form_pag = "PIX"
    elif form_pag == "03":
        form_pag = "BOLETO X1"
    elif form_pag == "":
        form_pag = "DINHEIRO"



    """INFORMAÇÕES DO CLIENTE"""

    sleep(2)
    print("=" * 45)
    print("\n\033[92mＰＥＤＩＤＯ ＤＥ ＶＥＮＤＡ\033[0m\n" \
    f"\nVENDEDOR: {vendedor['NOME']}\n"
    f"\nCLIENTE: {cliente}\n"
    f"CODIGO DE PAGAMENTO: {form_pag}")
    print("=" * 45)
    sleep(1)



    """MATERIAL"""
    while True:

        material = input("\nADICIONE O PRODUTO: ").upper()

        produto_encontrado = None
        for produto in estoque["cadastro"]:
            if produto["NOME"].upper() == material:
                produto_encontrado = produto
                break

        if produto_encontrado is None:
            print("\nPRODUTO NAO ENCONTRADO\n")
            continue


        ja_no_carrinho = sum(
            i["QUANT"] for i in itens if i["NOME"] == produto_encontrado["NOME"]
        )   
        disponivel = produto_encontrado["ESTOQUE"] - ja_no_carrinho
        preco = produto_encontrado["PRECO"]

        if disponivel <= 0:
            print("\nPRODUTO SEM ESTOQUE\n")
            continue

        print(f"\nPRODUTO: {produto_encontrado["NOME"]}\n")
        print(f"\nESTOQUE DISPONIVEL: {produto_encontrado["ESTOQUE"]}\n")
        print(f"\nPREÇO UNITARIO: {reais(preco)}")

        while True:
            try:
                quant = int(input("\nQUANTIDADE: "))
            except ValueError:
                print("\nPOR FAVOR DIGITE CERTO\n")
                continue

            if quant <= 0: 
                print("\nA QUANTIDADE DEVE SER MAIOR\n")
                continue

            if quant > disponivel:
                print("\nREVEJA A QUANTIDADE COLOCADA\n")
                continue

            break

        sub_total = round(quant * preco, 2)
        itens.append({
            "NOME": produto_encontrado["NOME"],
            "QUANT": quant,
            "PRECO": preco,
            "SUBTOTAL": sub_total
        })

        mais = input("\nADICIONAR MAIS PRODUTO: ").strip().upper()
        if mais != "S":
            break

    total = round(sum(i["SUBTOTAL"] for i in itens), 2)

    print("\n" + "=" * 45)
    print("\n         RESUMO DO PEDIDO\n")
    print("=" * 45)

    for i in itens:
        print(f"{i["NOME"]}")
        print(f" {i["QUANT"]} x {reais(i["PRECO"])} = {reais(i["SUBTOTAL"])}")
    print("-" * 45)
    print(f"TOTAL: {reais(total)}")
    print("=" * 45)


    sleep(2)
    confirmar = input("\nCONFIRMAR PEDIDO DE VENDA?: ").strip().upper()[:1]
    if confirmar != "S":
        print("\nPEDIDO CANCELADO\n")
        return

    for item in itens:
        for produto in estoque["cadastro"]:
            if produto["NOME"] == item["NOME"]:
                produto["ESTOQUE"] -= item["QUANT"]

    with open("dados/estoque.json", "w", encoding="utf-8") as arq:
        json.dump(estoque, arq, indent=4, ensure_ascii=False)


    print("\n\033[1;94mＶＥＮＤＡ ＲＥＧＩＳＴＲＡＤＡ\033[0m\n")
        
                    
                



        
                
                

    

    



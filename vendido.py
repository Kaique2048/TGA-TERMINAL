from time import sleep
import json


def pedido_venda(vendedor):

    with open("estoque.json", "r", encoding="utf-8") as arquivo:
        estoque = json.load(arquivo)
    

    lista = []


    cliente = input("\nNOME:").upper()

    if cliente == "":
            cliente = "CONSUMIDOR"
            print("\n\033[91mNAO DEIXE DE COLOCAR O NOME\033[0m\n")
    else:
        print()



    form_pag = input("FORMA DE PAGAMENTO:")

    if form_pag == "01":
        form_pag = "DINHEIRO"
    elif form_pag == "02":
        form_pag = "BOLETO"




    sleep(2)
    print("\n\n\033[92mＰＥＤＩＤＯ ＤＥ ＶＥＮＤＡ\033[0m  \n" \
    f"\nVENDEDOR: {vendedor['NOME']}\n"
    f"CLIENTE: {cliente}\n"
    f"CODIGO DE PAGAMENTO: {form_pag}")


    #MATERIAL
    while True:

        material = input("ADICIONE O PRODUTO: ")
        quant = int(input("QUANTIDADE: "))

        produto_encontrado = False

        for produto in ["cadastro"]:

            if material == produto["NOME"].upper():

                produto_encontrado = True

                print(f"PRODUTO: {produto['NOME']}")
                print(f"ESTOQUE DISPONIVEL: {produto["ESTOQUE"]}")

            while True:

                try:
                    quant = int(input("QUANTIDADE: "))

                    if quant <= 0:
                        print("A QUANTIDADE DEVE SER MAIOR")
                        continue

                    if quant > produto["ESTOQUE"]:
                        print("REVEJA, QUANTIDADE INSUFICIENTE")


                    break
                
                except ValueError:
                    print("DIGITE APENAS NUMEROS")
                    
             



            
                 
                 

        

        


    
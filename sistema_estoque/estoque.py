import json
import msvcrt
from time import sleep

def ESTOQUE():

    try:
        with open("dados/estoque.json", "r", encoding="utf-8") as arquivo:
            estoque = json.load(arquivo)

    except FileNotFoundError:
        estoque = {
            "cadastro": []
            }


    #LOOP DE SELEÇÃO
    while True:

        print("_" * 35)
        print('\n𝐒𝐈𝐒𝐓𝐄𝐌𝐀 𝐃𝐄 𝐄𝐒𝐓𝐎𝐐𝐔𝐄\n')

        #CADASTRAR PRODUTO 
        print('\n\033[32m|ＭＯＳＴＲＡＲ ＥＳＴＯＱＵＥ    |\033[0m\n'
              '\n\033[32m|ＣＡＤＡＳＴＲＡＲ ＰＲＯＤＵＴＯ|\033[0m \n' \
        '\n\033[32m|ＥＮＴＲＡＤＡ                   |\033[0m\n' \
        '\n\033[32m|ＳＡＩＤＡ                       |\033[0m')

        #SELECIONAR FUNÇÃO AUTOMATIZADA
        print("\n\033[31mSelecione\033[0m: ", end="", flush=True )
        selecionar = msvcrt.getche().decode("utf-8").upper()

        #PERCORRER ITEM POR ITEM DENTRO DO ESTOQUE
        if selecionar == "1":

            print("")
            print("\nＥＳＴＯＱＵＥ ＤＥ ＭＡＴＥＲＩＡＬ")

            for produto in estoque["cadastro"]:
                ID = produto["ID"]
                NOME = produto["NOME"]
                QUANTIDADE = produto["ESTOQUE"]
                PRECO = produto["PRECO"]


                print(f"\n\033[32m|ＩＤ\033[0m: {ID}")
                print(f"\033[32m|ＮＯＭＥ\033[0m: {NOME}")
                print(f"\033[32m|ＱＵＡＮＴＩＤＡＤＥ\033[0m: {QUANTIDADE}")
                print(f"\033[32m|PRECO: R$\033[0m{PRECO}")
                sleep(0.7)
            sleep(5)
            return
                
        
        #CADASTRAR PRODUTO, ITEM, MATERIAL
        elif selecionar == "2":

            print('')
            print('\n \033[91m ＰＲＯＤＵＴＯ \033[0m     ')
            print("\n \033[92m【C】【A】【D】【A】【S】【T】【R】【A】【R】\033[0m")

            ID = input("\nID: ")
            NOME = input("NOME: ").upper()
            QUANTIDADE = int(input("ESTOQUE: "))
            PRECO = float(input("PREÇO: R$").replace(",", "."))

            item = {
                    "ID": ID,
                    "NOME": NOME,
                    "ESTOQUE": QUANTIDADE,
                    "PRECO": PRECO
            
                }


            produto_encontrado = False 

            #SE JA ESTIVER O PRODUTO NO ESTOQUE, ELE VAI APENAS ADICIONAR A QUANTIDADE
            for produto in estoque["cadastro"]:
                if produto["ID"] == ID:
                    produto["ESTOQUE"] += QUANTIDADE
                    produto_encontrado = True
                    break

            #SE NAO TIVER O PRODUTO NO ESTOQUE VAI ADICIONAR O PRODUTO NO ESTOQUE
            if not produto_encontrado:
                estoque["cadastro"].append(item)

            with open("dados/estoque.json", "w", encoding="utf-8") as arquivo:
                json.dump(estoque, arquivo, indent=4, ensure_ascii=False)

            print("\n\033[1;94mPRODUTO CADASTRADO\033[0m\n")
            return

        elif selecionar == "3":
            print('')
            print("\n \033[92m【E】【N】【T】【R】【A】【D】【A】\033[0m")

            #PROCURA SABER DO ITEM E DA QUANTIDADE
            ADD_ITEM = input("\nNOME: ").upper( )
            ADD_QUANTI = int(input("ADICIONAR QUANTIDADE: "))

            #MANTEM O PRODUTO COMO FALSO(NAO ENCONTRADO)
            produto_encontrado2 = None

            #PROCURA O ITEM PELA LISTA PARA ADICIONAR
            for produto2 in estoque["cadastro"]:
                    if produto2["NOME"] == ADD_ITEM:
                        produto2["ESTOQUE"] += ADD_QUANTI
                        produto_encontrado2 = produto2
                        break   

            #ADICIONA A QUANTIDADE NO ITEM DA LISTA 
            if produto_encontrado2:
                with open("dados/estoque.json", "w", encoding="utf-8") as arquivo:
                    json.dump(estoque, arquivo, indent=4, ensure_ascii=False)


                print(f"O PRODUTO {produto_encontrado2["NOME"]}\n" \
                F"TEVE {ADD_QUANTI} ADICIONADO")

            else:
                print("PRODUTO NÃO ENCONTRADO")


        elif selecionar == "4":

            #ENTRADA COM NOME PERSONALIZADO VERDE
            print('')
            print("\n\033[92m【S】【A】【I】【D】【A】\033[0m")

            s_item = input("\nNOME:").upper()
            s_quant = int(input("QUANTIDADE: "))

            produto_encontrado3 = False

            #VERIFICA SE O ITEM ESTA NA LISTA E RETIRA A QUANTIDAE
            for produto3 in estoque["cadastro"]:
                if produto3["NOME"] == s_item:
                    produto3["ESTOQUE"] -= s_quant

                    produto_encontrado3 = True
                    break

            #SALVA O ARQUIVO ESTOQUE.JSON
            if produto_encontrado3:
                with open("dados/estoque.json", "w", encoding="utf-8") as arquivo:
                    json.dump(estoque, arquivo, indent=4, ensure_ascii=False)

            #NOME PERSONALIZADO PRA AVISAR QUE O ESTOQUE ESTA NEGATIVO
            if produto3['ESTOQUE']  < 0:
                print("\n\033[91mESTOQUE INSUFICIENTE!\033[0m")
                print("\n\033[91mPOR FAVOR DE ENTRADA!\033[0m")
        
            else:
                print("\033[31mRETIRADO COM SUCESSO\033[0m")

        #RETORNAR PARA O MENU INICIAL
        elif selecionar == "S":
            sleep(2)
            return
        

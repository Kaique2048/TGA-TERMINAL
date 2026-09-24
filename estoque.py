import json
import msvcrt
from time import sleep

def ESTOQUE():

    try:
        with open("estoque.json", "r", encoding="utf-8") as arquivo:
            estoque = json.load(arquivo)

    except FileNotFoundError:
        estoque = {
            "cadastro": []
            }


    #LOOP DE SELEÇÃO
    while True:

        print('\n𝐒𝐈𝐒𝐓𝐄𝐌𝐀 𝐃𝐄 𝐄𝐒𝐓𝐎𝐐𝐔𝐄\n')

        #CADASTRAR PRODUTO 
        print('\n|ＣＡＤＡＳＴＲＡＲ ＰＲＯＤＵＴＯ| \n' \
        '\n|ＥＮＴＲＡＤＡ                   |\n' \
        '\n|ＳＡＩＤＡ                       |')

        #SELECIONAR FUNÇÃO AUTOMATIZADA
        print("\nSelecione: ", end="", flush=True )
        selecionar = msvcrt.getche().decode()


        #CADASTRAR PRODUTO, ITEM, MATERIAL
        if selecionar == "1":

            print('')
            print('\n \033[91m ＰＲＯＤＵＴＯ \033[0m     ')
            print("\n \033[92m【C】【A】【D】【A】【S】【T】【R】【A】【R】\033[0m")

            ID = input("\nID: ")
            NOME = input("NOME: ").upper()
            QUANTIDADE = int(input("ESTOQUE: "))


            item = {
                    "ID": ID,
                    "NOME": NOME,
                    "ESTOQUE": QUANTIDADE
            
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

            with open("estoque.json", "w", encoding="utf-8") as arquivo:
                json.dump(estoque, arquivo, indent=4, ensure_ascii=False)

            print("\nPRODUTO CADASTRADO\n")
            return

        elif selecionar == "2":
            print('')
            print("\n \033[92m【E】【N】【T】【R】【A】【D】【A】\033[0m")

            #PROCURA SABER DO ITEM E DA QUANTIDADE
            ADD_ITEM = input("ID: ")
            ADD_QUANTI = int(input("ADICIONAR QUANTIDADE: "))

            #MANTEM O PRODUTO COMO FALSO(NAO ENCONTRADO)
            produto_encontrado2 = False

            #PROCURA O ITEM PELA LISTA PARA ADICIONAR
            for produto2 in estoque["cadastro"]:
                if produto2["ID"] == ADD_ITEM:
                    produto2["ESTOQUE"] += ADD_QUANTI

                #SE ENCONTRAR ELE ATUALIZA PARA ACHADO
                produto_encontrado2 = True
                break    

            #ADICIONA A QUANTIDADE NO ITEM DA LISTA 
            if produto_encontrado2:
                with open("estoque.json", "w", encoding="utf-8") as arquivo:
                    json.dump(estoque, arquivo, indent=4, ensure_ascii=False)

            #PRINTA FALANDO O NOME DO ITEM E A QUANTIDADE ADICIONADA
            print(f"O produto {produto2['NOME']} teve {ADD_QUANTI} adicionado ")
            return


        elif selecionar == "3":

            #ENTRADA COM NOME PERSONALIZADO VERDE
            print('')
            print("\n\033[92m【S】【A】【I】【D】【A】\033[0m")

            s_item = input("\nID:")
            s_quant = int(input("QUANTIDADE: "))

            produto_encontrado3 = False

            #VERIFICA SE O ITEM ESTA NA LISTA E RETIRA A QUANTIDAE
            for produto3 in estoque["cadastro"]:
                if produto3["ID"] == s_item:
                    produto3["ESTOQUE"] -= s_quant

                produto_encontrado3 = True
                break

            #SALVA O ARQUIVO ESTOQUE.JSON
            if produto_encontrado3:
                with open("estoque.json", "w", encoding="utf-8") as arquivo:
                    json.dump(estoque, arquivo, indent=4, ensure_ascii=False)

            #NOME PERSONALIZADO PRA AVISAR QUE O ESTOQUE ESTA NEGATIVO
            if produto3['ESTOQUE']  < 0:
                print("\n\033[91mESTOQUE INSUFICIENTE!\033[0m")
                print("\n\033[91mPOR FAVOR DE ENTRADA!\033[0m")
        
            else:
                print("RETIRADO COM SUCESSO")

        #RETORNAR PARA O MENU INICIAL
        elif selecionar == "s":
            sleep(2)
            return
        

#IMPORTANDO O CADASTRON.JSON(CADASTRO DE VENDEDOR)
import json
from datetime import datetime
from time import sleep
import msvcrt

"""IMPORTAÇÃO DE MODULOS"""
from sistema_cadastro.editar import ed_vend

def cad_vend():


    data_cadastro = datetime.now()
    
    #CARREGAR LISTA DE VENDEDORES
    with open("dados/cadastro.json", "r" ,encoding="utf-8") as arquivo:
        vendedores = json.load(arquivo)
    
    #PEGAR INFORMAÇÕES DO VENDEDOR
    while True:

        print("\n\033[32m|ＭＯＳＴＲＡＲ ＶＥＮＤＥＤＯＲＥＳ|\033[0m\n" \
        "\033[32m|ＣＡＤＡＳＴＲＡＲ                 |\033[0m\n" \
        "\033[32m|ＥＤＩＴＡＲ                       |\033[0m\n" \
        "\033[32m|ＥＸＣＬＵＩＲ                     |\033[0m")

        print("\n\033[31mSELECIONE\033[0m:", end="", flush=True)
        selecao = msvcrt.getche().decode("utf-8")


        
        
        if selecao == "1":
            print("\n\033[1;94mＭＯＳＴＲＡＮＤＯ ＶＥＮＤＥＤＯＲＥＳ ＣＡＤＡＳＴＲＡＤＯＳ\033[0m\n")

            for vendedor in vendedores["vendedores"]:
                CODIGO = vendedor["CODIGO"]
                NOME = vendedor["NOME"]
                DATA_CADASTRO = vendedor["DATA_CADASTRO"]

                print(f"CODIGO: {CODIGO}")
                print(f"NOME: {NOME}")
                print(f"DATA REGISTRADO: {DATA_CADASTRO}")
                print("-" * 30)
                sleep(2)
            sleep(2)
            return

        elif selecao == "2":

            while True:
                #TRATAMENTO DE ERROS
                try:
                    codigo = int(input("\n\nINFORME UM CODIGO VENDEDOR: "))

                except ValueError:
                    print("\n\033[91mＣＯＬＯＱＵＥ ＵＭ ＮＵＭＥＲＯ\033[0m\n")
                    sleep(2)
                    return

                    
                        
                Nome = str(input("INFORME O NOME DO VENDEDOR: "))


                if Nome == "":
                    print("\n\033[91mCOLOQUE O NOME POR FAVOR\033[0m\n")
                    sleep(2)

                elif len(Nome) < 8:
                    print("\n\033[91mPOR FAVOR COLOQUE O NOME COMPLETO\033[0m\n")
                    sleep(2)
                    return

                elif not Nome.replace(" ", "").isalpha():
                    print("\n\033[91mCOlOQUE APENAS LETRAS\033[0m\n")
                    sleep(2)

                else:
                    Nome = Nome.upper()

                #TRANSFORMANDO DATA HORA E MINUTO
                data_cadastro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                vendedor = {
                    "CODIGO": codigo,
                    "NOME": Nome,   
                    "DATA_CADASTRO": data_cadastro
                }
                #ADICIONANDO O VENDEDOR A LISTA
                vendedores["vendedores"].append(vendedor)

                #CARREGANDO E ADICIONANDO AO JSON
                with open("dados/cadastro.json", "w", encoding="utf-8") as arquivo:
                    json.dump(vendedores, arquivo, indent=4, ensure_ascii=False)

                #VENDEDOR CADASTRADO
                print(f"\n\033[94m|𝐕𝐄𝐍𝐃𝐄𝐃𝐎𝐑: {Nome}|\033[0m\n"
                    f"\033[94m|𝐂𝐎𝐃𝐈𝐆𝐎: {codigo}|\033[0m")

                
                print("\n \033[92mＶＥＮＤＥＤＯＲ ＣＡＤＡＳＴＲＡＤＯ\033[0m")
                return
        elif selecao == "3":
            ed_vend()

        elif selecao == "4":
            print("\nＥＸＣＬＵＳＡＯ ＤＥ ＶＥＮＤＥＤＯＲ")

            encontrado = False


            ID_EXCLUIR = int(input("\nCODIGO: "))
            sleep(1)

            for vendedor in vendedores["vendedores"]:
                if vendedor["CODIGO"] == ID_EXCLUIR:
                    vendedores["vendedores"].remove(vendedor)
                    encontrado = True
                    break

            if encontrado:
                with open("dados/cadastro.json", "w", encoding="utf-8") as arquivo:
                    json.dump(vendedores, arquivo, indent=4, ensure_ascii=False)

                print("\nＶＥＮＤＥＤＯＲ ＥＸＣＬＵＩＤＯ")

            else:

                print("ＶＥＮＤＥＤＯＲ ＮＡＯ ＥＮＣＯＮＴＲＡＤＯ")


        elif selecao == "s" or "S":
            return


            

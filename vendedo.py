#IMPORTANDO O CADASTRON.JSON(CADASTRO DE VENDEDOR)
import json
from datetime import datetime
from time import sleep


def cad_vend():


    data_cadastro = datetime.now()
    
    #CARREGAR LISTA DE VENDEDORES
    with open("cadastro.json", "r" ,encoding="utf-8") as arquivo:
        vendedores = json.load(arquivo)
    
    #PEGAR INFORMAÇÕES DO VENDEDOR
    while True:

            #TRATAMENTO DE ERROS
            try:
                codigo = int(input("INFORME UM CODIGO VENDEDOR: "))
                break

            except ValueError:
                print("\n\033[91mＣＯＬＯＱＵＥ ＵＭ ＮＵＭＥＲＯ\033[0m\n")
                sleep(2)

            
    while True:   
        Nome = str(input("INFORME O NOME DO VENDEDOR: "))


        if Nome == "":
            print("\n\033[91mCOLOQUE O NOME POR FAVOR\033[0m\n")
            sleep(2)

        elif len(Nome) < 8:
             print("\n\033[91mPOR FAVOR COLOQUE O NOME COMPLETO\033[0m\n")
             sleep(2)

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
        with open("cadastro.json", "w", encoding="utf-8") as arquivo:
            json.dump(vendedores, arquivo, indent=4, ensure_ascii=False)

        #VENDEDOR CADASTRADO
        print(f"\033[94m|𝐕𝐄𝐍𝐃𝐄𝐃𝐎𝐑: {Nome}|\033[0m\n"
              f"\033[94m|𝐂𝐎𝐃𝐈𝐆𝐎: {codigo}|\033[0m")

        
        print("\n \033[92mＶＥＮＤＥＤＯＲ ＣＡＤＡＳＴＲＡＤＯ\033[0m")
        return
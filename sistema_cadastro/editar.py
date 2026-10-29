import json

def ed_vend():
    with open ("dados/cadastro.json", "r", encoding="utf-8") as arq:
        cadastro = json.load(arq)


    nome_busca = input("\n\nNOME DO VENDEDOR: ").upper()

    vendedor_encontrado = False

    for vendedor in cadastro["vendedores"]:

        if vendedor["NOME"] == nome_busca:

            vendedor_encontrado = True

            print("\n\033[92mＶＥＮＤＥＤＯＲ ＥＮＣＯＮＴＲＡＤＯ\033[0m\n")
            print("=" * 35)
            print(f"CODIGO: {vendedor["CODIGO"]}")
            print(f"NOME: {vendedor["NOME"]}")
            print(f"DATA REGISTRADO: {vendedor["DATA_CADASTRO"]}")
            print("=" * 35)


            nv_nome = input("\nNOVO NOME: ").upper()
            nv_cd = int(input("NOVO CODIGO: "))

            vendedor["NOME"] = nv_nome
            vendedor["CODIGO"] = nv_cd

            break

    if vendedor_encontrado:

        with open("dados/cadastro.json", "w", encoding="utf-8") as arq:
            json.dump(cadastro, arq, indent=4, ensure_ascii=False)


        print("VENDEDOR ATUALIZADO COM SUCESSO")
        
        return

    else:
        print("\nVENDEDOR NAO ENCONTRADO")
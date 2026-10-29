def reais(valor):
    """FORMATA 1234.5 COMO R$1.234.50"""
    texto = f"{valor:,.2f}"
    return "R$ " + texto.replace(",", "X").replace(".", ",").replace("X", ".")


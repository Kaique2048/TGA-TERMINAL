from time import sleep


def escrever(texto, velocidade=0.03):
    for letra in texto:
        print(letra, end="", flush=True)
        sleep(velocidade)
    print()
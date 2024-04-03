import random

def alfabeto():
    lista = []
    for i in range(97, 123):
        lista.append(chr(i))
    return lista


def gera_chave():
    chave = {}
    letras = alfabeto()

    letras_cifradas = alfabeto()
    random.shuffle(letras_cifradas)

    for char, char_cifrado in zip(letras, letras_cifradas):
        chave[char] = char_cifrado

    return chave


def cripto(mensagem, chave):
    mensagem_cifrada = ""
    for char in mensagem:
        mensagem_cifrada += chave[char]

    return mensagem_cifrada

chave = gera_chave()
print(chave)
print(cripto("olamundo", chave))

def decripto(mensagem, chave):
    chave_inversa = {}
    for ch, vl in chave.items():
        chave_inversa[vl] = ch

    return cripto(mensagem, chave)

def main():
    chave = gera_chave()
    print(chave)
    while True:
        msg = input("Mensagem: ")
        op = input("1 para cifrar, 2 para sair, outro para decifrar: ")
        if op == "2":
            break
        if op == "1":
            print(cripto(msg, chave))
        else:
            print(decripto(msg, chave))
main()
pauta = {
    # chave: valor
    "a": 4.0,
    "b": 5.5,
    "c": 9.2,
    "d": 8.7,
    "e": 6.6
}

print(pauta)
print(pauta.keys())
print(pauta.values())

if "h" in pauta:
    print(pauta["h"])

# iterar pelas chaves -> o uso do .keys() é dispensável
for aluno in pauta:
    print(aluno)

# iterar pelos valores
for nota in pauta.values():
    print(nota)

# iterar pelo dicionário inteiro
for aluno, nota in pauta.items():
    print(aluno, nota)
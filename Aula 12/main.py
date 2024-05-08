from agencia import Agencia
from gerente import Gerente

ger1 = Gerente("Zé", "zé@gmail.com", "1234")
ag1 = Agencia(1, "Barra", ger1)

c1 = ag1.abrir_nova_conta("João")
c2 = ag1.abrir_nova_conta("Maria")

print(c1)
print(c2)

ag2 = Agencia(2, "Centro", ger1)

c3 = ag2.abrir_nova_conta("Carlos")

print(c3)

print(ag1)

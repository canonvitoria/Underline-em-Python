#Um breve estudo sobre 0 que é o Underline no python...
#Underline solto como se fosse uma variável que você não iria usar
#Dois exemplos:

#Exemplos do for ->

compras = [
    (100, 'fone ouvido'), #Valor de compra e o produto
    (200, 'mouse'),
    (5000, 'notebook'),
    (6000, 'iphone')
]

valor_total = 0

for valor, _ in compras:
    valor_total += valor

print(valor_total)

#Segundo exemplo ->

compras = [
    (100, 'fone ouvido'), #Valor de compra e o produto
    (200, 'mouse'),
    (5000, 'notebook'),
    (6000, 'iphone')
]

def pegar_compra(i):
    return compras[i]
_, produto = pegar_compra(1)

print(produto)

#https://youtu.be/2UokUrOlB7A
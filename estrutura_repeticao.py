# estrutura_repeticao.py
# Objetivo: demonstrar estruturas de repetição for e while

# Exemplo com for: somar números de 1 a 5
soma = 0
for i in range(1, 6):
    soma += i
print("Soma de 1 a 5 usando for:", soma)

# Exemplo com while: adicionar números a uma lista até chegar em 5
lista = []
contador = 1
while contador <= 5:
    lista.append(contador)
    contador += 1

print("Lista criada com while:", lista)

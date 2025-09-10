# lista_dict.py
# Objetivo: manipular listas e dicionários (adicionar, atualizar, remover elementos)

# Trabalhando com listas
frutas = ["maçã", "banana"]
frutas.append("laranja")          # adicionar elemento
frutas[1] = "uva"                 # atualizar por índice
frutas.remove("maçã")             # remover elemento

print("Lista de frutas:", frutas)

# Trabalhando com dicionários
pessoa = {"nome": "Ana", "idade": 25}
pessoa["idade"] = 26              # atualizar valor
pessoa["cidade"] = "Rio"          # adicionar nova chave
del pessoa["nome"]                # remover chave

print("Dicionário pessoa:", pessoa)

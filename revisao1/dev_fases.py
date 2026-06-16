"""variavel que recebe entrada via input
e imprime o nome da tela
"""
nome = input("Digite seu nome: ")
print(f"Ola,", {nome})

# Fase 2 - Lista e laço while
# Agora guardamos varios nomes
nomes= []

#While cria um laço infinito - so para com "break"
while True:
    nome = input("Digite um nome (ou 'sair' para terminar):")
    if nome == 'sair':
        break

    nomes.append(nome)

for n in nomes:
        print(n)

        #Fase 3 - Busca de nomes
busca = input("pesquisar nome:")
# 'in' verifica se o valor existe dentro da lista
if busca in nomes:
    print(f"{busca} encontrado")
else:
    print(f"{busca} nao esta na lista")

# 'for' é usado para percorrer toda lista (banco de Dados)

for i, n in enumerate(nomes, 1):
     print(f"{i}. {n}")


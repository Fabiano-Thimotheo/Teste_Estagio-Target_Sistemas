nome = input("Digite o seu nome: ")
nome_invertido = ""

for i in range(len(nome)-1, -1, -1):
    nome_invertido += nome[i]

print("O seu nome ao contrário é: ", nome_invertido)

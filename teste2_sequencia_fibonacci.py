# Solicitando ao usuário um número entre 1 e 100
num = int(input("Digite um número entre 1 e 100: "))

# Verificando se o número pertence à sequência de Fibonacci
a, b = 0, 1

while b < num:
    a, b = b, a+b

# Exibindo mensagem de acordo com o resultado
if b == num:
    print("O número digitado pertence à sequência de Fibonacci!")
else:
    print("Desculpe, mas o número digitado NÃO pertence à sequência de Fibonacci!")

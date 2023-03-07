# Importa o módulo 'json' para trabalhar com arquivos JSON
import json

# Abre o arquivo 'dados_teste_3.json' contendo os dados de faturamento diário da distribuidora
arquivo = open('dados_teste_3.json', 'r')
dados = json.load(arquivo)
arquivo.close()

# Encontra o menor e o maior valor de faturamento ocorrido no mês
valores = []
for dia in dados:
    valores.append(dia['valor'])

menor_valor = valores[0]
maior_valor = valores[0]

for valor in valores:
    if valor < menor_valor:
        menor_valor = valor
    elif valor > maior_valor:
        maior_valor = valor

# Calcula a média mensal de faturamento, desconsiderando os dias sem faturamento
soma = 0
qtd_dias_com_faturamento = 0

for dia in dados:
    if dia['valor'] > 0:
        soma += dia['valor']
        qtd_dias_com_faturamento += 1

media = soma / qtd_dias_com_faturamento

# Calcula o número de dias em que o valor de faturamento diário foi superior à média mensal
qtd_dias_acima_da_media = 0

for dia in dados:
    if dia['valor'] > media:
        qtd_dias_acima_da_media += 1

# Exibe em tela os resultados obtidos em formato de tabela, organizados por dia do mês
print('Dia:     Valor de faturamento:')
for dia in dados:
    print(f'{dia["dia"]:2}       R${dia["valor"]:,.2f}')
print()
print(f'Menor valor de faturamento no mês: R${menor_valor:,.2f}')
print(f'Maior valor de faturamento no mês: R${maior_valor:,.2f}')
print(f'Média mensal de faturamento:      R${media:,.2f}')
print(f'Número de dias acima da média:    {qtd_dias_acima_da_media}')

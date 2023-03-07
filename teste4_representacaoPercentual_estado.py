# Definindo o faturamento de cada estado
faturamento_sp = 67836.43
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 27165.48
faturamento_outros = 19849.53

# Calculando o faturamento total da distribuidora
faturamento_total = faturamento_sp + faturamento_rj + \
    faturamento_mg + faturamento_es + faturamento_outros

# Exibindo o faturamento total da distribuidora
print("Faturamento Mensal da Distribuidora: R${:,.2f}".format(
    faturamento_total))

# Calculando e exibindo a representatividade de cada estado no faturamento total da distribuidora
percentual_sp = (faturamento_sp / faturamento_total) * 100
percentual_rj = (faturamento_rj / faturamento_total) * 100
percentual_mg = (faturamento_mg / faturamento_total) * 100
percentual_es = (faturamento_es / faturamento_total) * 100
percentual_outros = (faturamento_outros / faturamento_total) * 100

print("Representatividade de cada estado no faturamento total:")
print("SP: {:.2f}%".format(percentual_sp))
print("RJ: {:.2f}%".format(percentual_rj))
print("MG: {:.2f}%".format(percentual_mg))
print("ES: {:.2f}%".format(percentual_es))
print("Outros: {:.2f}%".format(percentual_outros))
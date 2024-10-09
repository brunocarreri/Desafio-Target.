'''3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, 
que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.'''

import json

# abrindo arquivo json, codificando para formato de leitura UTF-8, apelidando o json de "arquivo".
with open('dados.json', encoding='utf-8') as arquivo:
    # inicializando a variavel com os dados tratados.
    dados = json.load(arquivo)

# realizando a soma de todos itens "valor" da lista que possuirem o valor maior que 0.
soma = sum(item['valor'] for item in dados if item['valor'] > 0)

# contando os dias que possuem o valor de faturamento maior que 0.
dias_com_faturamento = sum(1 for item in dados if item['valor'] > 0)

# calculando a média através dos dias que possuem faturamento
media = soma / dias_com_faturamento

# calculando a quantidade de dias maior que a média mensal.
dias_com_faturamento_superior_a_media = sum(
    1 for item in dados if item['valor'] > media)

print("Faturamento mensal: ", soma)

print("Media dos dias de faturamento: ", media)

print("total de dias com faturamento: ", dias_com_faturamento)

print("Dias com faturamento maior que a média mensal: ",
      dias_com_faturamento_superior_a_media)

'''4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP  R$67.836,43
• RJ  R$36.678,66
• MG  R$29.229,88
• ES  R$27.165,48
• Outros  R$19.849,53
Escreva um programa na linguagem que desejar onde calcule o percentual de 
representação que cada estado teve dentro do valor total mensal da distribuidora.
'''

# criando biblioteca das cidades com os valores.
cidades = [
    {'sp': 67836.43},
    {'rj': 36678.66},
    {'mg': 29229.88},
    {'es': 27164.48},
    {'outros': 19849.53}
]

# realizando a soma de todas as cidades.
soma = sum(next(iter(cidade.values())) for cidade in cidades)

print(f"A soma do valor total da distribuidora é: R${soma:.2f}")

# inserindo a biblioteca em um loop for para tratamento.
for cidade in cidades:

    if 'sp' in cidade:
        valor_sp = cidade['sp']
        print(f"O valor de SP é: R${valor_sp}")

        porcentagem_sp = (valor_sp / soma)*100

        print(f"Com a porcentagem de: %{porcentagem_sp:.2f}")

    elif 'rj' in cidade:
        valor_rj = cidade['rj']
        print(f"O valor do RJ é: R${valor_rj}")

        porcentagem_rj = (valor_rj / soma)*100

        print(f"Com a porcentagem de: %{porcentagem_rj:.2f}")

    elif 'mg' in cidade:
        valor_mg = cidade['mg']
        print(f"O valor de MG é: R${valor_mg}")

        porcentagem_mg = (valor_mg / soma)*100

        print(f"Com a porcentagem de: %{porcentagem_mg:.2f} ")

    elif 'es' in cidade:
        valor_es = cidade['es']
        print(f"O valor de ES é: R${valor_es}")

        porcentagem_es = (valor_es / soma)*100

        print(f"Com a porcentagem de: %{porcentagem_es:.2f}")

    elif 'outros' in cidade:
        valor_outros = cidade['outros']
        print(f"O valor de outras cidade é de: R${valor_outros}")

        pocentagem_outros = (valor_outros / soma)*100

        print(f"Com a porcentagem de: %{pocentagem_outros:.2f}")

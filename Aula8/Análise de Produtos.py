import pandas as pd
import yaml
import matplotlib.pyplot as plt

# Carregar o arquivo YAML
with open("empresa.yaml", "r") as file:
    dados = yaml.safe_load(file)

# Extraindo os dados de vendas
vendas = dados["vendas"]

# Cálculando a quantidade total de vendas para cada produto
quantidade_por_produto = {}
for produto in vendas:
    quantidade = produto["quantidade"]
    nome_produto = produto["produto"]

    #  O if abaixo irá verificar se o produto correspondente a um determinado nome já está registrado em 'quantidade_por_produto'. Se já estiver, ele irá adicionar a quantididade atual do loop
    if nome_produto in quantidade_por_produto:
        quantidade_por_produto[nome_produto] += quantidade
    else:
        quantidade_por_produto[nome_produto] = quantidade

# Ordenar os produtos com base na quantidade vendida. A função lambda recebe uma tupla e retorna o segundo elemento
produtos_mais_vendidos = sorted(
    quantidade_por_produto.items(),
    key=lambda x: x[1],
    reverse=True,
)

# Extraindo e armazenando quantidade e nome dos produtos mais vendidos
nomes_produtos = [produto[0] for produto in produtos_mais_vendidos]
quantidades_produtos = [produto[1] for produto in produtos_mais_vendidos]

# Plot do gráfico
plt.figure(figsize=(10, 6))
plt.bar(nomes_produtos, quantidades_produtos, color="skyblue")
plt.xlabel("Produtos")
plt.ylabel("Quantidade Vendida")
plt.title("Produtos Mais Vendidos")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()



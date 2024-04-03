import pandas as pd
import yaml
import matplotlib.pyplot as plt

# Carregar o arquivo YAML
with open("empresa.yaml", "r") as file:
    dados = yaml.safe_load(file)

# Extraindo os dados de vendas
vendas = dados['vendas']

receita_por_produto = {}

for produto in vendas:
    nome_produto = produto['produto']
    quantidade= produto['quantidade']
    preco_unitario = produto['preco_unitario']
    receita = quantidade * preco_unitario

    if nome_produto in receita_por_produto:
        receita_por_produto[nome_produto] += receita
    else:
        receita_por_produto[nome_produto] = receita

# Plotando gráfico de pizzas
labels = receita_por_produto.keys()
valores = receita_por_produto.values()

plt.figure(figsize=(8, 8))
plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição da Receita por Produto')
plt.axis('equal')  # Assegura que o gráfico de pizza seja desenhado como um círculo.
plt.show()
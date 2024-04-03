import pandas as pd
import yaml
import matplotlib.pyplot as plt

# Carregar o arquivo YAML
with open("empresa.yaml", "r") as file:
    dados = yaml.safe_load(file)

# Converter os dados em um DataFrame
df_vendas = pd.DataFrame(dados["vendas"])

# Printando as primeiras linhas do DataFrame
print(df_vendas.head())

# Converter a coluna de datas para o tipo datetime
df_vendas["data"] = pd.to_datetime(df_vendas["data"])

# Calcular o total de vendas para cada produto ao longo do tempo
# groupby é o responsável por agrupar todas as linhas que têm a mesma combinação de valores nas colunas (data e produto)
df_total_vendas = df_vendas.groupby(["data", "produto"]).sum().reset_index()

# Plotar o total de vendas para cada produto ao longo do tempo
fig, ax = plt.subplots(figsize=(10, 6))

# Cria o gráfico de barras a partir do agrupamento por produto e calcular a soma da quantidade vendida
df_total_vendas.groupby("produto")["quantidade"].sum().plot(kind="bar", ax=ax)

ax.set_title("Total de Vendas por Produto")
ax.set_xlabel("Produto")
ax.set_ylabel("Quantidade")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

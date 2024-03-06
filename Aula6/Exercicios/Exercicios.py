import numpy as np
import matplotlib.pyplot as plt

# Inicializando as matrizes

#  Dados fictícios de preços médios diários para duas ações (em dólares)
preco_medio_acao1 = np.array([50, 52, 48, 55, 53, 51, 49, 50, 54, 52])
preco_medio_acao2 = np.array([120, 122, 118, 125, 123, 121, 119, 120, 124, 122])

# Número de ações que o investidor possui de cada empresa
acoes_acao1 = 100  # Exemplo: o investidor possui 100 ações da Ação 1
acoes_acao2 = 50  # Exemplo: o investidor possui 50 ações da Ação 2

# Calculando o valor do investimento em cada dia
valor_investimento_1 = np.dot(acoes_acao1, preco_medio_acao1)
valor_investimento_2 = np.dot(acoes_acao2, preco_medio_acao2)

i1 = 1
for valor in valor_investimento_1:
    print(f"Ao final do dia {i1}, o valor do investimento será de: {valor}")
    i1 += 1

print("\n")

i2 = 1
for valor in valor_investimento_2:
    print(f"Ao final do dia {i2}, o valor do investimento será de: {valor}")
    i2 += 1

# Calculando o patrimônio total do investidor em cada dia
valor_patrimonio = valor_investimento_1 + valor_investimento_2

print("\n")

i3 = 1
for patrimonio in valor_patrimonio:
    print(
        f"Ao final do dia {i3}, o valor total de seu patrimônio será de: {patrimonio}"
    )
    i3 += 1


# Plot o gráfico da evolução patrimonial do investidor
dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.plot(dias, valor_patrimonio, marker="o")
plt.title('Evolução patrimonial do investidor')
plt.xlabel('Dias')
plt.ylabel('Patrimônio')
plt.grid(True)
plt.show()

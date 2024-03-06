import numpy as np

# Criação de Arrays:


# Inicializando uma matriz vazia
print("Exercício 1:")
empty_array = np.empty((3, 3))
print(empty_array)

# Inicializando uma matriz preenchida com valores iguais a 1
print("\n" "\n" "Exercício 2:")
ones_array = np.ones((2, 2))
print(ones_array)

# Inicializando uma matriz preenchida com valores iguais a 0
print("\n" "\n" "Exercício 3:")
zeros_array = np.zeros((4, 4))
print(zeros_array)

# Inicializando uma matriz preenchida com valores aleatórios
print("\n" "\n" "Exercício 4:")
random_array = np.random.rand(3, 3)
print(random_array)

# Seleciona o elemento na segunda linha e terceira coluna (6)
print("\n" "\n" "Exercício 5:")
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_array[1, 2])

# Para encontrar o valor máximo e mínimo em uma matriz
print("\n" "\n" "Exercício 6:")
max_value = np.max(my_array)
min_value = np.min(my_array)
print(f"Valor máximo: {max_value}, Valor mínimo: {min_value}")

# Para calcular a soma dos valores em uma matriz
print("\n" "\n" "Exercício 7:")
total_sum = np.sum(my_array)
print(f"Soma total: {total_sum}")


# =========================================================== #


# Manipulação de Arrays:


# Para remover entradas unidimensionais de uma matriz
print("\n" "\n" "Exercício 8:")
squeezed_array = np.squeeze(my_array)
print(squeezed_array)

# Adição de Matrizes
print("\n" "\n" "Exercício 9:")
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 + matriz2
print("Resultado da adição de matrizes:")
print(resultado)

# Subtração de Matrizes:
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 - matriz2
print("Resultado da subtração de matrizes:")
print(resultado)

# Multiplicação de Matrizes:
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = np.dot(matriz1, matriz2)
# Ou, alternativamente: resultado = matriz1 @ matriz2
print("Resultado da multiplicação de matrizes:")
print(resultado)
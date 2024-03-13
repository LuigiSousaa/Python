import pandas as pd

# Carrega o arquivo CSV em um DataFrame do Pandas
igm_df = pd.read_csv("igm_modificado/igm_modificado.csv")

# Imprime o DataFrame em formato de tabela (estrutura bidimensional)
print(igm_df)

# Imprime as 5 primeiras linhas e colunas. E transpõe (inverte coluna e linha)
print(igm_df.head().T)

# Obtém informações sobre o DataFrame, como tipos de dados e valores não nulos
igm_df.info()

# Exibe as 5 últimas linhas do DataFrame
igm_df.tail()

# Seleciona aleatoriamente 5 linhas do DataFrame
igm_df.sample(5)

# Seleciona as primeiras 5 linhas e colunas do DataFrame e transpõe
igm_df[0:5].T

# Seleciona as últimas 5 linhas e colunas do DataFrame e transpõe
igm_df[-5:].T

# Seleciona as linhas e colunas de 20 a 29 do DataFrame
igm_df[20:30]

# Seleciona a coluna 'porte' do DataFrame
igm_df['porte']

# Seleciona as colunas 'municipio' e 'indice_governanca' do DataFrame
igm_df[['municipio', 'indice_governanca']]

# Obtém o tipo de dados da coluna 'porte'
type(igm_df['porte'])

# Conta a quantidade de cada valor único na coluna 'porte'
igm_df['porte'].value_counts()

# Seleciona a coluna 'indice_governanca' do DataFrame
ind_des = igm_df['indice_governanca']

# Conta a quantidade de valores não nulos na coluna 'indice_governanca'
ind_des.count()

# Retorna o número total de elementos na coluna 'indice_governanca'
ind_des.size

# Verifica quais valores na coluna 'indice_governanca' são nulos
ind_des.isnull()

# Conta a quantidade de valores nulos na coluna 'indice_governanca'
ind_des.isnull().sum()

# Remove os valores nulos da coluna 'indice_governanca'
ind_des_notnull = ind_des.dropna(inplace=True)

import pandas as pd
import yaml
import matplotlib.pyplot as plt


# Carregar os dados dos funcionários a partir do arquivo YAML
with open('Aula7/dados_funcionarios.yaml', 'r') as file:
    dados_yaml = yaml.safe_load(file)


# Converter para DataFrame
df = pd.DataFrame(dados_yaml['funcionarios'])
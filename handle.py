import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('Result.csv')

# Adicionar a coluna 'handleId' com os valores 'Product_1', 'Product_2', etc.
df['handleId'] = ['Product_' + str(i+1) for i in range(len(df))]

# Salvar o arquivo CSV com a nova coluna
df.to_csv('Result_updated.csv', index=False)

print("Coluna 'handleId' adicionada com sucesso!")

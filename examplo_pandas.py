
import pandas as pd
import warnings

# Ignore deprecation warnings from pandas
warnings.filterwarnings('ignore', category=DeprecationWarning, module='.')


df = pd.read_csv('detalhe_cobertura.csv')
print("\nDataFrame\n")
print(df)
print("-----------------------------------------------")


result = df.groupby('cobertura_id')['valor'].sum().reset_index()

result.rename(columns={'valor': 'valor_total'}, inplace=True)

print("\nResultado total\n")
print(result)
print("-----------------------------------------------")

# Converter a coluna 'date' para datetime
df['date'] = pd.to_datetime(df['date'])


# Converter a coluna datetime para timestamp para facilitar a comparação
df['timestamp'] = df['date'].astype('int64') // 10**6

# Função para filtrar eventos próximos dentro de 600ms
def filter_events(group):
    diffs = group['timestamp'].diff().abs()
    mask = (diffs > 600) | (diffs.isna())
    return group[mask]

# Aplicar a função de filtro em cada grupo de cobertura_id
filtered_data = df.groupby('cobertura_id').apply(filter_events).reset_index(drop=True)

# Remover a coluna de timestamp auxiliar
filtered_data.drop('timestamp', axis=1, inplace=True)

# Agrupar por 'cobertura_id' e somar os 'valors'
result = filtered_data.groupby('cobertura_id')['valor'].sum().reset_index()

# Renomear a coluna de soma para refletir o conteúdo
result.rename(columns={'valor': 'valor_total'}, inplace=True)
print("\nResultado dispensando eventos proximos:\n")
print(result)

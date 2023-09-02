import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Passo 1: Carregar a base de dados
df = pd.read_csv("./Dataset/crimes.dataset.csv")

# Passo 2: Tratamento de dados (vamos remover as colunas desnecessárias)
columns_to_drop = ['Violent Crimes', 'Violent crime rate',
                   'Murder nonnegligent manslaughter',
                   'Murder nonnegligent manslaughter rate', 'Rape\n(revised\ndefinition)',
                   'Rape\n(revised\ndefinition)\nrate', 'Rape\n(legacy\ndefinition',
                   'Rape\n(legacy\ndefinition)\nrate', 'Robbery\nrate',
                   'Aggravated\nassault', 'Aggravated\nassault rate', 'Property\ncrime',
                   'Property\ncrime\nrate', 'Burglary\nrate', 'Larceny-\ntheft',
                   'Larceny-\ntheft rate', 'Motor\nvehicle\ntheft',
                   'Motor\nvehicle\ntheft\nrate']

df = df.drop(columns=columns_to_drop)
df['Population'] = df['Population'].str.replace(',', '').astype(float)
# Imprime informações sobre o DataFrame após o tratamento
info_df = df.info()
print(info_df)

# Passo 3: Definir variáveis preditoras (X) e variável dependente (y)
X = df[["Year"]]  # Ano como variável preditora
y = df["Population"]  # População como variável de destino

# Passo 4: Análise dos dados
print(df.describe())

# Passo 5: Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Passo 6: Aplicar um modelo de regressão linear
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_y_pred = lr_model.predict(X_test)

# Métricas de avaliação
lr_rmse = mean_squared_error(y_test, lr_y_pred, squared=False)
lr_r2 = r2_score(y_test, lr_y_pred)

# Crie um dicionário com as métricas
metricas = {
    'Métrica': ['RMSE', 'R^2'],
    'Regressão Linear': [lr_rmse, lr_r2],
    # Adicione as métricas de outros modelos aqui, se necessário
}

# Crie um DataFrame a partir do dicionário
metricas_df = pd.DataFrame(metricas)

# Imprima o DataFrame
print("Métricas de Avaliação do Modelo:")
print(metricas_df)

print("Regressão Linear - RMSE:", lr_rmse)
print("Regressão Linear - R^2:", lr_r2)

# Passo 7: Plotar gráfico de valores reais vs. valores previstos
plt.scatter(X_test, y_test, color='blue', label='Valores Reais')
plt.plot(X_test, lr_y_pred, color='red', linewidth=2, label='Valores Previstos (Regressão Linear)')
plt.xlabel("Ano")
plt.ylabel("População")
plt.legend()
plt.title("Valores Reais vs. Valores Previstos (Regressão Linear)")
plt.show()

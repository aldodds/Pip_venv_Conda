import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Aquí 'ruta/datos.csv' es la ruta a tu archivo CSV
df = pd.read_csv('datos.csv')

# 1. Sumar la producción total por mes
produccion_mensual = df[['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']].sum()

# 2. Gráfico de barras de la producción mensual
plt.figure(figsize=(10, 6))
produccion_mensual.plot(kind='bar', color='skyblue')
plt.title('Producción Total de Cultivos por Mes')
plt.xlabel('Mes')
plt.ylabel('Producción Total')
plt.xticks(rotation=45)

# 3. Gráfico de cajas (boxplot) de la producción mensual
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']])
plt.title('Distribución de la Producción de Cultivos por Mes')
plt.xlabel('Mes')
plt.ylabel('Producción')

# 4. Agregar una columna con la producción total por fila (registro)
df['Total_Produccion'] = df[['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']].sum(axis=1)

# 5. Agrupar por año y sumar la producción total por año
produccion_por_ano = df.groupby('Año_EVA')['Total_Produccion'].sum()

# Mostrar todas las gráficas al final
plt.show()

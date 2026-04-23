import pandas as pd

df = pd.read_csv("1ventas.csv")

df["fecha"] = pd.to_datetime(df["fecha"])

df["dia_semana"] = df["fecha"].dt.dayofweek
df["mes"] = df["fecha"].dt.month

df = df.dropna()

df.to_csv("ventas_procesado.csv", index=False)

print("Preprocesamiento completado")

# Este codigo lo que hace es limpiar los datos y los deja listos para usar
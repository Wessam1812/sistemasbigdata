import pandas as pd
import pickle
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("ventas_procesado.csv")

X = df[["promocion", "temperatura", "dia_semana", "mes"]]
y = df["ventas"]

#abre la IA que se guardo antes
model = pickle.load(open("modelo.pkl", "rb"))

#intenta predecir ventas
pred = model.predict(X)

mae = mean_absolute_error(y, pred)
rmse = np.sqrt(mean_squared_error(y, pred))
r2 = r2_score(y, pred)

print("MAE:", mae)
print("RMSE:", rmse)
print("R2:", r2)

# mae --> error medio 
# rmse --> penaliza errores grandes
# r2 --> calidad del modelo
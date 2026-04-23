import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# lee los datos limpios
df = pd.read_csv("ventas_procesado.csv")


# aqui separa los datos en lo que el modelo usa para pensar (en este caso x) 
# para predecir las ventas (y)
X = df[["promocion", "temperatura", "dia_semana", "mes"]]
y = df["ventas"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#crea el modelo
model = RandomForestRegressor(n_estimators=100)

#Aqui la IA aprende de los datos
model.fit(X_train, y_train)

#lo guarda
pickle.dump(model, open("modelo.pkl", "wb"))

print("Modelo entrenado correctamente")
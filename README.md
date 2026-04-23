# Proyecto Sistemas Big Data - SuperFresh

## Pasos para que funcione
1. Ejecutar requirements.txt --> pip install -r requirements.txt
2. Ejecutar 2procesamiento.py --> se crea el archivo ventas_procesados.csv
3. Ejecutar 3modelo_random_forest.py --> se crea modelo.pkl
4. Ejecutar 4evaluacion_modelo.py --> como de bien funciona el modelo
5. Ejecutar 5spark_procesamiento.py --> tener todo organizado simulando una gran cantidad de datos
6. Ejecutar 7app.py --> ver la venta futura

## API
http://127.0.0.1:5000/predict?promocion=1&temperatura=20&dia_semana=2&mes=5

### promocion: 1 = sí, 0 = no
### temperatura: valor numérico según el clima
### dia_semana: 0–6 (lunes a domingo)
### mes: 1–12

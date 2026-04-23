import psycopg2

conn = psycopg2.connect(
    database="superfresh",
    user="postgres",
    password="1812",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ventas (
    fecha DATE,
    producto TEXT,
    ventas INT,
    promocion INT,
    temperatura INT
)
""")

conn.commit()
conn.close()

print("Base de datos configurada")
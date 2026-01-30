from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from psycopg.rows import dict_row
from pydantic import BaseModel
import psycopg
import os

app = FastAPI()

# Variables de entorno - Aquí es donde Docker inyecta los datos
host = os.environ.get("DB_HOST")
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
dbname = os.environ.get("DB_NAME","postgres")
port = os.environ.get("DB_PORT", "5432")

# Conexion a la base de datos
try: 
    conn = psycopg.connect(
        host=host,
        user=user,
        password=password,
        dbname=dbname,
        port=port,
        row_factory=dict_row 
    )

    with conn.cursor() as cursor:
        cursor.execute("create table if not exists mensajes (id serial primary key, mensaje text, autor text)")
        conn.commit()
        print("¡Tabla mensajes verificada/creada exitosamente!")
except Exception as e:
    print(f"Error de conexión: {e}")
    # No cerramos con exit() para que el contenedor no se muera y puedas ver el error
    conn = None

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Mensaje(BaseModel):
    mensaje: str
    autor: str

@app.get("/health")
def health():
    return {"status": "ok", "db_connected": conn is not None}

@app.get("/data")
def data():
    if not conn: return {"error": "DB no conectada"}
    with conn.cursor() as cursor:
        cursor.execute("select * from mensajes")
        return cursor.fetchall()

@app.post("/save")
def save(mensaje: Mensaje):
    if not conn: return {"error": "DB no conectada"}
    with conn.cursor() as cursor:
        cursor.execute("insert into mensajes (mensaje, autor) values (%s, %s)", (mensaje.mensaje, mensaje.autor))
        conn.commit()
        return {"status": "guardado"}

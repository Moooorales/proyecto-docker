import psycopg._copy_async
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from psycopg.rows import dict_row
from pydantic import BaseModel
import psycopg
import os


app = FastAPI()

# Variables de entorno
host = os.environ.get("DB_HOST")
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
dbname = os.environ.get("DB_NAME","postgres")
port = os.environ.get("DB_PORT",5432)

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

    # Crear la tabla si no existe
    with conn.cursor() as cursor:
        cursor.execute("create table if not exists mensajes (id serial primary key, mensaje text, autor text)")
        conn.commit()
        print("Tabla mensajes creada exitosamente!")
except Exception as e:
    print(f"Error al conectar a la base de datos, revise las variables de entorno: {e}")
    print("Variables de entorno obligatorias:")
    print("DB_HOST")
    print("DB_USER")
    print("DB_PASSWORD")
    print("DB_NAME")
    print("DB_PORT")
    exit()

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Entidad Mensaje
class Mensaje(BaseModel):
    mensaje: str
    autor: str

def getdata():
    try:
        with conn.cursor() as cursor:
            cursor.execute("select * from mensajes")
            rows = cursor.fetchall()
            return rows
    except Exception as e:
        print(f"Error al obtener los datos: {e}")
        return {"error": str(e)}

def save_data(mensaje: str, autor: str):
    try:
        with conn.cursor() as cursor:
            cursor.execute("insert into mensajes (mensaje, autor) values (%s, %s)", (mensaje, autor))
            conn.commit()
            return {"mensaje":mensaje, "autor":autor}
    except Exception as e:
        print(f"Error al guardar el mensaje: {e}")
        return {"error": str(e)}

@app.post("/save")
def save(mensaje: Mensaje):
    return save_data(mensaje.mensaje, mensaje.autor)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/data")
def data():
    return getdata()

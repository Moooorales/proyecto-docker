cat <<EOF > README.md
# 🚀 Servicio Backend - FastAPI & PostgreSQL

Este proyecto es una API robusta construida con **FastAPI** y **PostgreSQL**, totalmente contenedorizada mediante **Docker**. El sistema permite gestionar mensajes con persistencia de datos y cuenta con validación automática.

## 🛠️ Tecnologías utilizadas
* **Lenguaje:** Python 3.11
* **Framework:** FastAPI
* **Base de Datos:** PostgreSQL
* **Infraestructura:** Docker & Docker Compose
* **Librerías clave:** Psycopg, Pydantic, Dotenv

## 🏗️ Arquitectura de Archivos
* \`Dockerfile\`: Configuración de la imagen del servidor.
* \`docker-compose.yml\`: Orquestación de los servicios (Backend + DB).
* \`server.py\`: Lógica de la API y conexión a la base de datos.
* \`.env.example\`: Plantilla de variables de entorno.

## 🚀 Instalación y Ejecución

1. Clonar el repositorio.
2. Levantar los contenedores:
   \`\`\`bash
   docker compose up --build
   \`\`\`
3. El servicio estará disponible en: [http://localhost:8000](http://localhost:8000)

## 📁 Endpoints Principales
* **GET \`/health\`**: Verifica el estado del servidor y la conexión a la DB.
* **POST \`/save\`**: Guarda un nuevo mensaje (requiere JSON).
* **GET \`/data\`**: Lista todos los mensajes almacenados.

---
Desarrollado por **Isaac** - Proyecto de Backend 2026.
EOF

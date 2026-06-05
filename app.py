import time
from flask import Flask
import psycopg2

app = Flask(__name__)

VERSION = "2.0.0"

@app.route("/")
def inicio():
    conexion = None
    retries = 5
    
    # Bucle de resistencia para esperar a que Postgres despierte
    while retries > 0:
        try:
            conexion = psycopg2.connect(
                host="db",
                database="empresa",
                user="admin",
                password="admin123"
            )
            break
        except psycopg2.OperationalError:
            retries -= 1
            time.sleep(2)

    if not conexion:
        return "<h1>Error de conexión</h1><p>No se pudo establecer conexión con PostgreSQL.</p>"

    try:
        cursor = conexion.cursor()
        
        # 1. Ejecutamos la consulta para traer a los clientes de la Actividad 4
        cursor.execute("SELECT id, nombre FROM clientes;")
        lista_clientes = cursor.fetchall()
        
        # 2. Traemos la versión de Postgres (para mantener tu estructura original)
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()

        cursor.close()
        conexion.close()

        # 3. Construimos la lista en HTML dinámicamente
        html_clientes = "".join([f"<li><strong>ID {c[0]}:</strong> {c[1]}</li>" for c in lista_clientes])

        return f"""
        <h1>Aplicación Flask (DevOps)</h1>
        <h2>Versión {VERSION}</h2>
        <hr>
        <h3>Listado de Clientes (Desde Postgres):</h3>
        <ul>
            {html_clientes if html_clientes else "<li>No hay clientes registrados aún.</li>"}
        </ul>
        <hr>
        <p><strong>Detalle del Motor:</strong> {db_version[0]}</p>
        """
    except Exception as e:
        return f"<h1>Error en la consulta</h1><p>{str(e)}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
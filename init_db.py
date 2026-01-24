import sqlite3
import os

# Ruta de la base de datos
default_db = "coches.db" if os.name == "nt" else "/sqlite3-db/coches.db"
db_path = os.environ.get("DB_PATH", default_db)

# Limpiar comillas si vienen de entorno
db_path = db_path.strip().strip('"').strip("'")

# Crear directorio si hace falta (Docker)
db_dir = os.path.dirname(db_path)
if db_dir and db_dir not in (".", "./", ".\\"):
    os.makedirs(db_dir, exist_ok=True)

# Conexión a la base de datos
connection = sqlite3.connect(db_path)
cur = connection.cursor()

# ===========================
# CREAR TABLAS (SI NO EXISTEN)
# ===========================
with open("coches.sql") as f:
    connection.executescript(f.read())

# ===========================
# COMPROBAR SI YA HAY DATOS
# ===========================
cur.execute("SELECT COUNT(*) FROM marcas")
num_marcas = cur.fetchone()[0]

if num_marcas == 0:
    # ===========================
    # INSERTS PARA TABLA MARCAS
    # ===========================
    cur.execute("""
    INSERT INTO marcas (id, nombre, pais, fundador, anio_fundacion)
    VALUES (1, 'Toyota', 'Japón', 'Kiichiro Toyoda', 1937)
    """)

    cur.execute("""
    INSERT INTO marcas (id, nombre, pais, fundador, anio_fundacion)
    VALUES (2, 'Ford', 'Estados Unidos', 'Henry Ford', 1903)
    """)

    cur.execute("""
    INSERT INTO marcas (id, nombre, pais, fundador, anio_fundacion)
    VALUES (3, 'BMW', 'Alemania', 'Karl Rapp', 1916)
    """)

    # ===========================
    # INSERTS PARA TABLA COCHES
    # ===========================
    cur.execute("""
    INSERT INTO coches (id, modelo, id_marca, anio, tipo_motor, potencia)
    VALUES (1, 'Corolla', 1, 2020, 'Gasolina', 132)
    """)

    cur.execute("""
    INSERT INTO coches (id, modelo, id_marca, anio, tipo_motor, potencia)
    VALUES (2, 'Mustang', 2, 2019, 'Gasolina', 450)
    """)

    cur.execute("""
    INSERT INTO coches (id, modelo, id_marca, anio, tipo_motor, potencia)
    VALUES (3, 'M3', 3, 2021, 'Gasolina', 480)
    """)

    print("Base de datos inicializada con datos de ejemplo.")
else:
    print("La base de datos ya estaba inicializada. No se insertaron datos.")

connection.commit()
connection.close()

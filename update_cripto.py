from sqlalchemy import create_engine, text
import pandas as pd

# Configuración de la base de datos MySQL
db_config = {
    'host': 'localhost',
    'usuario': 'root',
    'contraseña': 'Zaq12wsx.',
    'base_de_datos': 'cripto_db'  # Ahora nos conectamos a 'cripto_db'
}

# Crear la cadena de conexión
cadena_conexion = (
    f"mysql+mysqlconnector://{db_config['usuario']}:{db_config['contraseña']}@"
    f"{db_config['host']}/{db_config['base_de_datos']}"
)

# Crear el motor de SQLAlchemy
engine = create_engine(cadena_conexion)

# Crear la tabla 'crypto_prices' si no existe
with engine.connect() as connection:
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS crypto_prices (
            timestamp DATETIME PRIMARY KEY,
            price FLOAT,
            moving_avg FLOAT
        )
    """))

# Datos de ejemplo (simulando datos procesados)
data = {
    'timestamp': ['2023-10-01 12:00:00', '2023-10-02 12:00:00'],
    'price': [50000, 51000],
    'moving_avg': [49000, 50000]
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Cargar el DataFrame en la tabla 'crypto_prices'
df.to_sql('crypto_prices', con=engine, if_exists='append', index=False)

print("Datos cargados en la tabla 'crypto_prices' de la base de datos 'cripto_db'.")
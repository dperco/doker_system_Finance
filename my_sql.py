from sqlalchemy import create_engine, text

# Configuración de la base de datos MySQL
db_config = {
    'host': 'localhost',
    'usuario': 'root',
    'contraseña': 'Zaq12wsx.',
    'base_de_datos': 'cripto_db'  # Conéctate a una base de datos existente (por ejemplo, 'coderhouse')
}

# Crear la cadena de conexión
cadena_conexion = (
    f"mysql+mysqlconnector://{db_config['usuario']}:{db_config['contraseña']}@"
    f"{db_config['host']}/{db_config['base_de_datos']}"
)

# Crear el motor de SQLAlchemy
engine = create_engine(cadena_conexion)

# Crear la base de datos 'cripto_db' si no existe
with engine.connect() as connection:
    # Usar text() para ejecutar una consulta SQL directa
    connection.execute(text("CREATE DATABASE IF NOT EXISTS cripto_db"))

print("Base de datos 'cripto_db' creada o verificada con éxito.")
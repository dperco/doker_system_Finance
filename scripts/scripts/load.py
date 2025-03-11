
from sqlalchemy import create_engine
import pandas as pd

def load_data(df, table_name='stock_prices', db_config=None):
    """
    Carga los datos en una tabla de MySQL.
    
    Parámetros:
        df (pd.DataFrame): DataFrame con los datos a cargar.
        table_name (str): Nombre de la tabla en MySQL.
        db_config (dict): Configuración de la base de datos MySQL.
    """
    if db_config is None:
        raise ValueError("Se requiere la configuración de la base de datos MySQL.")

    # Crear la cadena de conexión para MySQL
    cadena_conexion = (
        f"mysql+mysqlconnector://{db_config['usuario']}:{db_config['contraseña']}@"
        f"{db_config['host']}/{db_config['base_de_datos']}"
    )

    # Crear el motor de SQLAlchemy
    engine = create_engine(cadena_conexion)

    # Cargar el DataFrame en la tabla de MySQL
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

    print(f"Datos cargados en la tabla '{table_name}' de MySQL.")
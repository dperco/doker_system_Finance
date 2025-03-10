# pipeline.py
# # from prefect import flow, task
# # from extract import fetch_crypto_data
# # from transform import transform_data
# # from load import load_data

# # @task
# # def extract():
# #     return fetch_crypto_data()

# # @task
# # def transform(df):
# #     return transform_data(df)

# # @task
# # def load(df):
# #     load_data(df)

# # @flow
# # def crypto_etl():
# #     data = extract()
# #     transformed_data = transform(data)
# #     load(transformed_data)

# # if __name__ == "__main__":
# #     crypto_etl()

# pipeline.py
from scripts.extract import fetch_crypto_data
from scripts.transform import transform_data
from scripts.load import load_data

# Configuración de la base de datos MySQL
db_config = {
    'host': 'localhost',
    'usuario': 'root',
    'contraseña': 'Zaq12wsx.',
    'base_de_datos': 'cripto_db'
}

# Extraer datos de la API
print("Extrayendo datos de la API...")
df = fetch_crypto_data(coin_id='bitcoin', vs_currency='usd', days='30')

# Transformar los datos
print("Transformando los datos...")
df_transformed = transform_data(df)

# Cargar los datos en MySQL
print("Cargando los datos en MySQL...")
load_data(df_transformed, table_name='crypto_prices', db_config=db_config)

print("Proceso ETL completado con éxito.")
# extract.py
# scripts/extract.py
# import requests
# import pandas as pd

# def fetch_crypto_data(coin_id='bitcoin', vs_currency='usd', days='30'):
#     url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
#     params = {
#         'vs_currency': vs_currency,
#         'days': days
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         data = response.json()
#         prices = data['prices']
#         df = pd.DataFrame(prices, columns=['timestamp', 'price'])
#         df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
#         return df
#     else:
#         raise Exception(f"Error fetching data: {response.status_code}")


import requests
import pandas as pd

def fetch_stock_data(symbol='IBM', api_key=''):
    """
    Obtiene datos diarios de una acción usando la API de Alpha Vantage.
    
    Parámetros:
        symbol (str): Símbolo de la acción (por ejemplo, 'IBM').
        api_key (str): Tu clave API de Alpha Vantage.
    
    Retorna:
        pd.DataFrame: Un DataFrame con los datos diarios de la acción.
    """
    url = "https://www.alphavantage.co/query"
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key,
        'outputsize': 'compact',  # 'compact' para los últimos 100 datos, 'full' para todos los datos históricos
        'datatype': 'json'  # Puedes cambiar a 'csv' si prefieres trabajar con CSV
    }

    # Hacer la solicitud a la API
    response = requests.get(url, params=params)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        
        # Extraer la serie temporal diaria
        time_series = data.get('Time Series (Daily)', {})
        
        # Convertir los datos en un DataFrame
        df = pd.DataFrame.from_dict(time_series, orient='index')
        
        # Renombrar las columnas
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        
        # Convertir los índices a tipo datetime
        df.index = pd.to_datetime(df.index)
        
        # Convertir las columnas a tipo numérico
        df = df.apply(pd.to_numeric)
        
        return df
    else:
        raise Exception(f"Error fetching data: {response.status_code}")
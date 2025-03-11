
import pandas as pd

def transform_data(df):
    """
    Transforma los datos de la acción.
    
    Parámetros:
        df (pd.DataFrame): DataFrame con los datos de la acción.
    
    Retorna:
        pd.DataFrame: DataFrame transformado.
    """
    # Calcular el promedio móvil de 7 días
    df['moving_avg'] = df['close'].rolling(window=7).mean()
    
    return df
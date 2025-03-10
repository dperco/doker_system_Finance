# Dockerfile
# Dockerfile
FROM apache/airflow:2.5.0

# Copiar los scripts, DAGs y airflow.cfg al contenedor
COPY scripts/ /opt/airflow/scripts/
COPY dags/ /opt/airflow/dags/
COPY airflow.cfg /opt/airflow/airflow.cfg 


# Agrega la carpeta scripts al PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/scripts"
# Cambiar al usuario 'airflow' para instalar dependencias
USER airflow

# Instalar dependencias adicionales
RUN pip install --no-cache-dir pandas requests mysql-connector-python sqlalchemy

# Establecer el directorio de trabajo
WORKDIR /opt/airflow
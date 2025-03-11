# doker_system_Finance
# Stock ETL Pipeline with Airflow and Docker

This project is an ETL (Extract, Transform, Load) pipeline that extracts stock data from the Alpha Vantage API, transforms it, and loads it into a MySQL database. The pipeline is orchestrated using Apache Airflow and runs in a Dockerized environment.

## Table of Contents

1. Overview
2. Prerequisites
3. Setup
4. Project Structure
5. Running the Pipeline
6. Accessing Airflow UI
7. Accessing MySQL
8. Customization
9. Troubleshooting
10. License

---

## Overview

This project demonstrates how to build an ETL pipeline using:
- Alpha Vantage API: To fetch stock data.
- Apache Airflow: To orchestrate the pipeline.
- MySQL: To store the transformed data.
- Docker: To containerize the application.

The pipeline consists of three main tasks:
1. Extract: Fetches stock data from the Alpha Vantage API.
2. Transform: Processes the data (e.g., calculates moving averages).
3. Load: Stores the data in a MySQL database.

---

## Prerequisites

Before running the project, ensure you have the following installed:
- Docker: Install Docker (https://docs.docker.com/get-docker/)
- Docker Compose: Install Docker Compose (https://docs.docker.com/compose/install/)
- Alpha Vantage API Key: Get your API key (https://www.alphavantage.co/support/#api-key)

---

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/stock-etl-pipeline.git
   cd stock-etl-pipeline
Replace TU_CLAVE_API in extract.py with your Alpha Vantage API key.

Build and start the Docker containers:

bash
Copy
docker-compose up -d --build
Project Structure
Copy
stock-etl-pipeline/
├── dags/
│   └── stock_etl_dag.py          # Airflow DAG definition
├── scripts/
│   ├── extract.py                # Script to fetch data from Alpha Vantage
│   ├── transform.py              # Script to transform the data
│   └── load.py                   # Script to load data into MySQL
├── Dockerfile                    # Dockerfile for Airflow
├── docker-compose.yml            # Docker Compose configuration
├── airflow.cfg                   # Airflow configuration file
└── README.md                     # This file
Running the Pipeline
Start the Docker containers:

bash
Copy
docker-compose up -d
Access the Airflow UI at http://localhost:8080.

Enable and trigger the stock_etl_pipeline DAG.

Monitor the pipeline execution in the Airflow UI.

Accessing Airflow UI
URL: http://localhost:8080

Username: admin

Password: admin

Accessing MySQL
Connect to the MySQL container:

bash
Copy
docker exec -it airflow-mysql /bin/bash
mysql -u root -pZaq12wsx. -D cripto_db
Query the stock_prices table:

sql
Copy
SELECT * FROM stock_prices;
Customization
Change the Stock Symbol
To fetch data for a different stock, update the symbol parameter in extract.py:

python
Copy
def extract():
    return fetch_stock_data(symbol='AAPL', api_key='TU_CLAVE_API')  # Change 'AAPL' to your desired stock symbol
Modify the Transformation Logic
Edit the transform.py file to customize the data transformation logic.

Change the Database Configuration
Update the db_config dictionary in crypto_etl_dag.py if you need to connect to a different MySQL database.

Troubleshooting
Airflow Container Fails to Start
Check the logs for errors:

bash
Copy
docker logs practica_doker-webserver-1
Ensure the MySQL container is running:

bash
Copy
docker ps
Data Not Loading into MySQL
Verify that the stock_prices table exists:

sql
Copy
SHOW TABLES;
Check the logs of the load task in the Airflow UI.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Alpha Vantage (https://www.alphavantage.co/) for providing the stock data API.



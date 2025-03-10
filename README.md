# doker_system_Finance
Financial Data ETL Pipeline with Docker, Airflow, and Alpha Vantage API
This project is a financial data ETL (Extract, Transform, Load) pipeline built using Docker, Apache Airflow, and the Alpha Vantage API. The pipeline extracts daily stock data, transforms it, and loads it into a MySQL database. The goal is to optimize the data ingestion process and ensure efficient and reliable data processing.

Table of Contents
Overview

Prerequisites

Setup

Step 1: Clone the Repository

Step 2: Obtain an Alpha Vantage API Key

Step 3: Configure the Environment

Step 4: Build and Run Docker Containers

Pipeline Workflow

Extract

Transform

Load

Optimizations

Accessing the Data

Troubleshooting

Contributing

License

Overview
This project demonstrates how to:

Use Docker to containerize the application and its dependencies.

Use Apache Airflow to orchestrate the ETL pipeline.

Extract financial data from the Alpha Vantage API.

Transform the data (e.g., calculate moving averages).

Load the data into a MySQL database.

The pipeline is designed to be scalable, efficient, and easy to maintain.

Prerequisites
Before you begin, ensure you have the following installed:

Docker and Docker Compose.

Python 3.8+.

An Alpha Vantage API Key (free tier available at Alpha Vantage).

Setup
Step 1: Clone the Repository
Clone this repository to your local machine:

bash
Copy
git clone [https://github.com/your-repo/financial-data-etl.git](https://github.com/your-repo/financial-data-etl.git)
cd financial-data-etl
Step 2: Obtain an Alpha Vantage API Key
Sign up for a free API key at Alpha Vantage.

Replace TU_CLAVE_API in the extract.py file with your actual API key.

Step 3: Configure the Environment
Create a .env file in the root directory with the following content:

env
Copy
AIRFLOW_UID=1000
AIRFLOW_GID=0
MYSQL_ROOT_PASSWORD=Zaq12wsx.
MYSQL_DATABASE=cripto_db
MYSQL_USER=root
MYSQL_PASSWORD=Zaq12wsx.
ALPHA_VANTAGE_API_KEY=your_api_key_here
Update the docker-compose.yml file if necessary (e.g., change MySQL credentials or Airflow configurations).

Step 4: Build and Run Docker Containers
Build and start the Docker containers:

bash
Copy
docker-compose up -d --build
Access the Airflow web interface at [http://localhost:8080](http://localhost:8080).

Default username: airflow

Default password: airflow

Trigger the stock_etl_pipeline DAG manually from the Airflow UI.

Pipeline Workflow
Extract
The extract.py script fetches daily stock data from the Alpha Vantage API using the TIME_SERIES_DAILY function. The data includes:

Open price

High price

Low price

Close price

Volume

Transform
The transform.py script performs transformations on the extracted data, such as calculating a 7-day moving average for the closing price.

Load
The load.py script loads the transformed data into a MySQL database table named stock_prices.

Optimizations
To optimize the data ingestion process:

Batch Processing: Fetch and process data in batches to avoid API rate limits.

Error Handling: Implement retries and error handling for API requests.

Parallel Execution: Use Airflow's ParallelTaskGroup to run tasks concurrently.

Logging: Add detailed logging for debugging and monitoring.

Data Validation: Validate data before loading it into the database.

Accessing the Data
Connect to the MySQL database:

bash
Copy
docker exec -it airflow-mysql /bin/bash
mysql -u root -pZaq12wsx. -D cripto_db
Query the stock_prices table:

sql
Copy
SELECT * FROM stock_prices;
Troubleshooting
Common Issues
API Rate Limits:

The free tier of Alpha Vantage allows only 5 requests per minute and 500 requests per day. Use batch processing or upgrade to a premium plan.

Docker Networking Issues:

Ensure all containers are on the same Docker network. Verify connectivity using ping or docker network inspect.

Airflow Logs Not Found:

Check the secret_key configuration and ensure all Airflow components are synchronized.

MySQL Table Not Created:

Verify that the load.py script is correctly configured and that the MySQL service is running.

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch for your feature or bugfix.

Submit a pull request with a detailed description of your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Alpha Vantage for providing the financial data API.

Apache Airflow for the workflow orchestration.

Docker for containerization.


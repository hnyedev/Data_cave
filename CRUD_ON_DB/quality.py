import pandas as pd
import mysql.connector
import psycopg2

# Connect to MySQL
mysql_conn = mysql.connector.connect(
    host="localhost",
    user="datauser",           # Use datauser from docker-compose
    password="datapass123",    # Use datapass123 from docker-compose
    database="sales_data_raw"  # Your actual database name
)

# Connect to PostgreSQL
pg_conn = psycopg2.connect(
    host="localhost",
    port=5435,
    user="datauser",
    password="rootpass123",
    database="employee_data_raw"  
)

# Quick quality check
customers_df = pd.read_sql("SELECT * FROM customers", mysql_conn)
employees_df = pd.read_sql("SELECT * FROM employees", pg_conn)

print("MySQL Customers - Missing Values:")
print(customers_df.isnull().sum())

print("\nPostgreSQL Employees - Missing Values:")
print(employees_df.isnull().sum())

mysql_conn.close()
pg_conn.close()

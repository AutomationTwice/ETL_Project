import pandas as pd
from sqlalchemy import create_engine

# Database configuration
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': '5432',
    'database': 'database_name'
}

# CSV file path
csv_file_path = 'path-to-csv-file'

# Create a connection to the PostgreSQL database
engine = create_engine(f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

# Extract data from CSV
data = pd.read_csv(csv_file_path)

# Load data into PostgreSQL
data.to_sql('your_table_name', engine, if_exists='replace', index=False)

print("ETL process completed successfully.")

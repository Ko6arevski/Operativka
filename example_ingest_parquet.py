import pandas as pd
from sqlalchemy import create_engine

# Step 1: Load Parquet file
df = pd.read_parquet('./users.parquet')

# Step 2: Connect to PostgreSQL
connection_string = "postgresql+psycopg2://your-username:your-password@your-host:your-port/your-database"
engine = create_engine(connection_string)

# Step 3: Ingest DataFrame to PostgreSQL
df.to_sql('your_table_name', engine, if_exists='replace', index=False)
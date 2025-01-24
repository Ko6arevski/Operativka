#Prepare the instance
sudo apt update
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv

# Create a virtual environment
python3 -m venv ./dbt
cd dbt/
source bin/activate


#Install PostgreSQL:
sudo apt install postgresql
#Start the PostgreSQL service:
sudo systemctl start postgresql
#Enable PostgreSQL to start on boot:
sudo systemctl enable postgresql
#Verify the installation:
psql --version
#Switch to the PostgreSQL user:
sudo -i -u postgres
#Create a new PostgreSQL user:
CREATE USER dbt WITH PASSWORD 'dbt';
#Connect to the PostgreSQL database:
psql
# Grant SUPERUSER role to the user 'dbt' (for testing purposes)
ALTER USER dbt WITH SUPERUSER;
# To connect with the new user
psql -U dbt -d postgres -h localhost -p 5432

# Install dbt
pip install dbt-core dbt-postgres
dbt init my_first_project
# Supply the credentials for the database
cd my_first_project
# Check if its working
dbt debug








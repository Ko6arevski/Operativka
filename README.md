# Operativka
Initial storage space for all scripts and bulshit we will come up with in the training sessions

## Structure
```bash
 tree -L 2
 
.
├── CLI FUs
│   └── git_commands.md
├── Hr_test_key.pem
├── Hristo_accessKeys.csv
├── README.md
└── aws_setup
    └── step-by-step_procedure.md
```

## Wishlist
Add here topics to cover on the sessions and we can prioritize them and mark as done

- [x] Git repository set up
- [ ] CI/CD (GitHub pipelines)
  - [ ] Linters
  - [ ] Add Git precomit checks
  - [ ] Other quality checks
  - [ ] Tests
- [ ] IDEs setup
- [ ] [DBT](https://www.getdbt.com/)
- [ ] [DataHub](https://datahubproject.io/) ([The github repo](https://github.com/datahub-project/datahub))
- [ ] [Apache Superset](https://superset.apache.org) (Open source reporting solution)
- [ ] AWS
  - [x] AWS EC2 instance
  - [x] AWS free tier databases (RDS)
  - [x] AWS S3
  - [ ] AWS Lambda
  - [ ] AWS Glue
  - [ ] AWS Athena
  - [ ] AWS Kinesis
  - [ ] AWS Redshift
  - [ ] AWS Sagemaker
  - [ ] AWS QuickSight
- [ ] Streamlit
- [ ] Install AirFlow server on a EC2 and link to a repository
- [ ] Create a container environment that can run Airflow
- [ ] Use the container environment on the EC2 with a pipeline
- [ ] [Ansible](https://www.ansible.com/)


```PowerShell
#Install Windows Subsystem for Linux (WSL) https://learn.microsoft.com/en-us/windows/wsl/install
wsl --install
```

```bash
# Clone the repository
git clone https://github.com/Ko6arevski/Operativka.git
```

## project ideas

### Daily exchange rates 
- We can use the central bank's API to pull the data
- Scheduling can be done with a cron job on a machine (EC2 or on-prem)
- We can use Kafka to "stream" the data even if we dont need to :D
- We can look to spin up an RDS to store the data
- We can use lambdas to explore serverless processing
- We can look into glue if we want to add some more actions
- We can start building on it with demographics data from Eurostat or other source

### imot.bg pricing live feed and analysis
- check for API or scraping is the only way
- bulk load and then incremental fill
- delete/update logic
- maybe plimit to a single area
- transform and store
- imement checks for average market prices, same property price updates, undervalued/overvalued
- automated newsletter and alerts

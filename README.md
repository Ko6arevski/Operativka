# Operativka
Initial storage space for all scripts and bulshit we will come up with in the training sessions


## Wishlist
Add here topics to cover on the sessions and we can prioritize them and mark as done

- [x] Git repository set up
- [ ] CI/CD
  - [ ] Linters
  - [ ] Other quality checks
  - [ ] Tests
- [ ] IDEs setup
- [ ] DBT
- [ ] AWS
  - [ ] AWS EC2 instance
  - [ ] AWS free tier databases (RDS)
  - [ ] AWS S3
  - [ ] AWS Lambda
  - [ ] AWS Glue
  - [ ] AWS Athena
  - [ ] AWS Kinesis
  - [ ] AWS Redshift
  - [ ] AWS Sagemaker
  - [ ] AWS QuickSight
- [ ] Streamlit
- [ ] Install AirFlow server on a EC2 and link to a repository
- [ ] Spin up and RDS and use as DB for Airflow
- [ ] Add Git precomit checks
- [ ] Look into GitHub pipelines and CI/CD setup
- [ ] Create a container environment that can run Airflow
- [ ] Use the container environment on the EC2 with a pipeline
- [ ] Apache Supoerset - https://superset.apache.org/ (Open source reporting solution)
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

### imot.bg pricing live feed and analysis
- check for API or scraping is the only way
- bulk load and then incremental fill
- delete/update logic
- maybe plimit to a single area
- transform and store
- imement checks for average market prices, same property price updates, undervalued/overvalued
- automated newsletter and alerts

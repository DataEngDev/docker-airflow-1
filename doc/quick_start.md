### Quick start

### Run

```bash

git clone https://github.com/DataEngDev/docker-airflow-1.git
cd docker-airflow-1
# run the service
docker-compose -f docker-compose.yml up -d

# down the service
docker-compose -f docker-compose.yml down
```
- Login to Airflow UI : localhost:8080
	- account : airflow
	- password : airflow

- Access Airflow backend DB (Postgre)


### QA inside Docker
```bash
docker ps -a 
# find the "airflow_scheduler" one 
docker exec -it <instance_id> bash
# QA command
```
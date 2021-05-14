## Credit Recovery API

Welcome! This is the repository of Credit Recovery API source code.

### Features
- You can consult Credit recovery cases;
- You can consult creditos and debtors users.

### Requirements

- Python 3
- Django 3

### Development setup

To setup this project for local development, you have to download the repository and download the docker containers.

### Poetry
You can use Poetry to run the project. 
More info about Poetry: <https://python-poetry.org/docs/>

```
python3 -m venv venv
source venv/bin/activate
poetry install
```

### Fast setup
1. Clone this repository in your machine.
   ```
   git clone https://github.com/marlonleite/credit_recovery.git
   ```
2. Navigate to the project root folder.
3. Download and install Docker.
   <https://www.docker.com/products/docker-desktop>
4. Go to the repository folder in your terminal and run:

```
docker volume create --name=credit_database
```
 and run:
   
```
docker-compose up -d
```
stop docker:
```
docker-compose down
```
5. Once the command is finished, run the following command to get the containers' ids:
``` 
docker container ls
```
OBS: You can drop and recreate `database` if build fails. 
Run that cmds:
```
docker-compose run --rm web bash
```
```
psql -h db -U postgres postgres -c "DROP DATABASE postgres"
```
```
psql -h db -U postgres postgres -c "CREATE DATABASE postgres"
```
Once the new database is created, run:
```
make migrate
```
```
make create_admin
```
6. Exit the container and make sure you are in the repository folder in the terminal.
7. Kill container and rerun docker-compose again:
```
docker-compose down
```
```
docker-compose up -d
```
8. Good, go to Credit Recovery API url:
```
http://0.0.0.0:8000/
```

### Running the tests

Some tests were done in the application.

Run the follow command:
```
pytest
```
or
```
pytest path/app/test
```

### Author
Marlon Leite - <https://github.com/marlonleite/>

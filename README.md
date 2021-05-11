## Credit Recovery API

Welcome! This is the repository of Credit Recovery API source code.

### Development setup

To setup this project for local development, you have to download the repository, download the docker containers and load a database dump.

### Fast setup
1. Clone this repository in your machine.
2. Navigate to the project folder on your local computer.
3. Download and install Docker.
4. Go to the repository folder in your terminal and run:

```
docker volume create --name=credit_database
```
4. Run - It might take a while to finish:
   
```
docker-compose up -d
```
5. Once the command is finished, run the following command to get the containers' ids:
``` 
docker container ls
```
6. Get the id of the postgres image and run the following command to enter in the container:
```
docker-compose run --rm web bash
```
7. Run the following two commands. Be aware that this command can fail sometimes because the database is currently being used by another images - such as the web container - and you need to stop these images.
```
psql -h db -U postgres postgres -c "DROP DATABASE credit_db"
psql -h db -U postgres postgres -c "CREATE DATABASE credit_db"
```
8. Once the new database is created, run:.
```
python manage.py migrate
python manage.py collectstatic
```
9. Exit the container and make sure you are in the repository folder in the terminal.
10. Kill container and rerun docker-compose again:
```
docker-compose up -d
```
11. To stop the containers run the command: `docker-compose down`
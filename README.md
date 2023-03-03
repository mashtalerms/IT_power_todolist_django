# IT Power test task #


## Mashtaler Maksim 02/03/2023
Backend for online application for monitoring the execution of tasks

# Description #


### Stack ###
- python3.9, Django - backend
- Postgres - database


## Features ##

1. Authentication (todolist/core)
   - django authentication
2. Main logic (todolist/goals)
   - full CRUD for boards, goals 
   - permissions are correctly configured to read/update/delete for all entities


## How to: ##

## Development local configuration ##
1) Create venv
2) Install dependencies
   - `pip install -r requirements.txt`
3) Run docker container for postgres
   - `docker-compose -f deploy/docker-compose.db.yaml up -d`
4) Make migrations
   - `cd todolist`
   - `manage.py makemigrations`
   - `manage.py migrate`
5) Run server 
   - `manage.py runserver`
6) Createsuperuser
   - `manage.py createsuperuser`
7) Connect to admin panel at http://127.0.0.1:8000/admin/


## Project links
1) Admin - http://127.0.0.1:8000/admin
2) Swagger - http://127.0.0.1:8000/api/schema/swagger-ui

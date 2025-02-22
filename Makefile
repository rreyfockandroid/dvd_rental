SHELL = /bin/bash
PG_PASS=root01
PYTHON=python3

db-start:
	docker start rental-postgres

db-stop:
	docker stop rental-postgres

app-run:
	$(PYTHON) manage.py runserver

gui-run:
	$(PYTHON) dvdrental/app/gui_app/main.py

penv:
	./scripts/activate_venv.sh
 #source venvdir/bin/activate

db-download:
	mkdir -p tmp; cd tmp; wget https://neon.tech/postgresqltutorial/dvdrental.zip; unzip dvdrental.zip; 
	# tar -xvf dvdrental.tar; rm dvdrental.zip dvdrental.tar

db-import:
	docker exec -i rental-postgres psql -U postgres -c "CREATE DATABASE dvdrental;"
	docker exec -i rental-postgres pg_restore -U postgres -d dvdrental /db_dump/dvdrental.tar

db-import-schema:
	docker exec -i rental-postgres psql -U postgres -d dvdrental -f /db_dump/restore.sql 

db-remove:
	docker network rm rental-network
	docker rm rental-postgres

db-network:
	docker network create rental-network

db-install: db-network
	docker run --name rental-postgres -v $(PWD)/tmp:/db_dump --network rental-network -p5432:5432 -e POSTGRES_PASSWORD=$(PG_PASS) -d postgres

db-client:
	docker run -it --rm --network rental-network postgres psql -h rental-postgres -U postgres

lib-freeze:
	pip freeze > requirements.txt

lib-install:
	pip install -r requirements.txt
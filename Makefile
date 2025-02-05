SHELL = /bin/bash
db-start:
	docker start some-postgres

app-run:
	python manage.py runserver

penv:
	./scripts/activate_venv.sh
	#source venvdir/bin/activate


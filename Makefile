SHELL = /bin/bash
db-start:
	docker start some-postgres

app-run:
	python manage.py runserver

penv:
	source venvdir/bin/activate


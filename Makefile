SHELL = /bin/bash
db-start:
	docker start some-postgres

app-run:
	python manage.py runserver

gui-run:
	python dvdrental/app/gui_app/main.py

penv:
	./scripts/activate_venv.sh
	#source venvdir/bin/activate


#base
docker exec -it some-postgres /bin/bash
psql -U postgres
\l
\c dvdrental
\d

#app https://docs.djangoproject.com/en/5.1/intro/tutorial01/
python3 -m venv venvdir
source venvdir/bin/activate
django-admin startproject mysite dvd_rental
python manage.py artapp polls
python manage.py migrate

python -m pip install Django
pip freeze > requirements.txt


git log --oneline

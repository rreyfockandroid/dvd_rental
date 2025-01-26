#base
docker exec -it some-postgres /bin/bash
psql -U postgres
\l
\c dvdrental
\d

#app
python3 -m venv venvdir
source venvdir/bin/activate

python -m pip install Django
pip freeze > requirements.txt

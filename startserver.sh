pip install -r requirements.txt
python3 manage.py makemigrations users notifications welcomejorney
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver &
python3 notions_demon/daemon.py start

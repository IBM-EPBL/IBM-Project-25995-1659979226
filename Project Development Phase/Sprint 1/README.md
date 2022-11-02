1)First create a virtual env using:
python -m venv env

2)Then activate it by using:
env/Scripts/activate

3)Then use the command to install the libraries required:
pip install -r ./requirements.txt

4)Then switch to myapp directory and run the commands:
python manage.py makemigrations
python manage.py migrate

(OPTIONAL) If an error showing 'api_user table not found', run the following command:
python manage.py migrate --run-syncdb

5)Finally run the app by using:
python manage.py runserver

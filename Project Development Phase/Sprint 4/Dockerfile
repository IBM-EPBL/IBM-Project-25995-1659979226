FROM python:latest
COPY ./myapp /myapp
COPY ./requirements.txt /requirements.txt
WORKDIR /myapp
RUN pip install -r /requirements.txt
RUN cd /myapp
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py migrate --run-syncdb
CMD [ "python","manage.py","runserver 0.0.0.0:8000"]
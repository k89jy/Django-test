
   
FROM python:3.6-alpine

MAINTAINER Benjamin Jung <bsjung@gmail.com>

EXPOSE 80

RUN apk add --no-cache gcc python3-dev musl-dev

ADD . /django_practice_prj

WORKDIR /django_practice_prj

RUN pip install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:80" ]
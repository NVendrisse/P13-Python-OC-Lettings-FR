# pull official base image
FROM python:3.12.8


# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0


# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000
# run gunicorn
# CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
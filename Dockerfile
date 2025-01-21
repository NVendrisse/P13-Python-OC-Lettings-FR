# pull official base image
FROM python:3.11.8
RUN --mount=type=secret,id=LOGIN,env=env
RUN --mount=type=secret,id=TOKEN,env=env

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
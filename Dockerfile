FROM python:3.12.3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt
RUN python3 manage.py collectstatic

EXPOSE 8000

ENTRYPOINT [ "python", "manage.py" ]
CMD [ "runserver", "0.0.0.0:8000" ]
FROM python:3.10.12-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . /app

# Set the working directory
WORKDIR /app

# Server
CMD ["python", "manage.py","runserver", "0.0.0.0:8000", "--settings=config.settings.production"]
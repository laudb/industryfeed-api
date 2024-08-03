FROM python:3.10.12-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONBUFFERED=1

RUN pip install --upgrade pip

RUN ls

COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . /app
WORKDIR /app


EXPOSE 8000

# Server
CMD ["python", "manage.py","runserver", "0.0.0.0:8000", "--settings=config.settings.production"]
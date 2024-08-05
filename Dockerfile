FROM python:3.10.12-slim-buster

# Set workind directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONBUFFERED=1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./runserver.sh .
RUN sed -i 's/\r$//g' /usr/src/app/runserver.sh
RUN chmod +x /usr/src/app/runserver.sh

# copy project
COPY . .

# Make port 8000 available externally
EXPOSE 8000

# Server
ENTRYPOINT ["/usr/src/app/runserver.sh"]
#!/bin/bash

if [ "$1" == "production" ]
then
    python3 manage.py runserver --settings=config.settings.production
elif [ "$1" == "test" ]
then
    python3 manage.py test feed/tests/ --settings=config.settings.test
else
    python3 manage.py runserver --settings=config.settings.local
fi
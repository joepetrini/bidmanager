#!/bin/bash
python manage.py sqlclear bids | ./manage.py dbshell && ./manage.py syncdb && ./manage.py loaddata fixtures/initial_data.json
python manage.py rebuild_index --noinput
python manage.py runserver 8001

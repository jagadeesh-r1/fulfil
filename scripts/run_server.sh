#!/bin/bash

cd /home/azureuser/fulfil/    #relace service_repowith  your repo name 

pip3 install -r requirements.txt

python3 manage.py runserver & celery -A fulfil worker -l INFO && kill $!

#!/bin/bash

cd /recipebook

./manage.py migrate
./manage.py runserver 0.0.0.0:8000

#!/bin/bash
echo "Запускаем сервер"
source venv/bin/activate
python3 yatube/manage.py migrate
python3 yatube/manage.py runserver


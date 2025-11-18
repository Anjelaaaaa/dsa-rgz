#!/bin/bash
python app.py 5001 &
python app.py 5002 &
python app.py 5003 &
echo "Запущено 3 сервера на портах 5001, 5002, 5003"
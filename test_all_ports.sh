#!/bin/bash

# Порт 5001
echo "Port 5001"
curl -X POST http://127.0.0.1:5001/analyze -H "Content-Type: application/json" -d '{"text":"It is a truth universally acknowledged that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood this truth is so well fixed in the minds of the surrounding families that he is considered as the rightful property of some one or other of their daughters"}'
echo -e "\n"

# Порт 5002
echo "Port 5002"
curl -X POST http://127.0.0.1:5002/analyze -H "Content-Type: application/json" -d '{"text":"Call me Ishmael. Some years ago never mind how long precisely having little or no money in my purse and nothing particular to interest me on shore I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation"}'
echo -e "\n"

# Порт 5003
echo "Port 5003"
curl -X POST http://127.0.0.1:5003/analyze -H "Content-Type: application/json" -d '{"text":"It was a bright cold day in April and the clocks were striking thirteen. Winston Smith his chin nuzzled into his breast in an effort to escape the vile wind slipped quickly through the glass doors of Victory Mansions though not quickly enough to prevent a swirl of gritty dust from entering along with him"}'
echo -e "\n"

# Nginx балансировка 
echo "Балансировка через nginx"
curl -X POST http://localhost/analyze -H "Content-Type: application/json" -d '{"text":"In my younger and more vulnerable years my father gave me some advice that I have been turning over in my mind ever since. Whenever you feel like criticizing any one he told me just remember that all the people in this world have not had the advantages that you have had"}'
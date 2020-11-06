#!/bin/bash

source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=flask_example.py
flask run -p 5000 -h 0.0.0.0

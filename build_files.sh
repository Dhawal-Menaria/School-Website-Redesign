#!/bin/bash
echo "==================BUILD START=================="
pip3 install -r requirements.txt
python3 manage.py migrate 
python3 manage.py collectstatic --noinput 
echo "==================BUILD END=================="

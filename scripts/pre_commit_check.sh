#!/bin/bash
source __/bin/activate

echo "# -------------------"
echo "# running nosetests"
echo "# -------------------"
nosetests --with-coverage --cover-erase --cover-inclusive

echo "# -------------------"
echo "# pyflakes"
echo "# -------------------"
pyflakes query_area.py

echo "# -------------------"
echo "# pylint"
echo "# -------------------"
pylint -d all -e W0611,W0612,W0613,W0614 --reports=n --msg-template='{msg_id} {path}:{line} {msg} ({symbol})' query_area.py

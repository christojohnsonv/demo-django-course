#!/bin/bash


if [-d "env"]
then
  echo "Python virtual env exists"
else
  apt install python3.10-venv
  python3 -m venv venv
fi

echo $PWD
source venv/bin/activate

pip3 install -r requirements.txt

if [-d "logs"]
then
  echo "Log folder exists"
else
  mkdir logs
  touch logs/error.log logs/access.log
fi

sudo chmod -R 777 logs

echo "env setup finished."

Make sure python is installed:

python --version

https://www.python.org/downloads/

Add python to path if needed

cd Databases_Term_Project

activate venv

  For Windows: venv\Scripts\activate
  
  For MacOS: source myvenv/bin/activate
  
cd CSCI4370_TP_prototype

Install necessary packages:

pip install django

pip install mysql

pip install mysqlclient

pip install mysql-connector-python

Inside your root local instance in MySQL, create a new schema called Thoughts.

Inside the settings.py file adjust the databases 'PASSWORD' to match your specific MySQL password.


To run the server Make sure you're in Databases_Term_Project/CSCI4370_TP_prototype:

python manage.py runserver

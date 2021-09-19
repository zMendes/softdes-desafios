FROM python:3.8
ADD . /usr/src/app
WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
RUN apt -y update && apt upgrade && apt -y install sqlite3 libsqlite3-dev

WORKDIR /usr/src/app/src/
RUN if [ -e quiz.db ]; then echo "Database already created"; else sqlite3 quiz.db < quiz.sql; fi 
RUN if [ -e users.csv ]; then python3 adduser.py; else echo "User file not found"; fi  

CMD ["python", "./softdes.py"]
# backend:v0.1

```
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip wheel setuptools
pip install mysql-connector-python
pip install flask
pip freeze > requirements.txt

CREATE DATABASE client;
USE client;
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON client .*  TO 'admin'@'localhost';
FLUSH PRIVILEGES;

SHOW tables;
DESC DATA;
SELECT * FROM DATA;


curl "http://localhost:8000/?name=name"
curl -X POST -H "Content-type: application/json" -d'{"name": "ali","email": "ali@mrsalehi.info"}' localhost:8000
curl -X DELETE -H "Content-type: application/json" -d'{"name": "ali","email": "ali@mrsalehi.info"}' localhost:8000

docker network create myapp
docker build -t backend:v0.2 .
docker run -d --name mysql --network=myapp -e MYSQL_ROOT_PASSWORD=admin -e MYSQL_DATABASE=client -e MYSQL_USER=admin -e MYSQL_PASSWORD=admin mysql
docker run --name backend --network=myapp -e host=mysql -e user=admin -e passwd=admin -e database=client -d -p 8000 backend:v0.2
```
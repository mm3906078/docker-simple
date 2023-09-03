# backend:v0.1

```
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip wheel setuptools
pip install flask
pip freeze > requirements.txt

curl "http://localhost:8000/?name=name"
curl -X PUT -H "Content-type: application/json" -d'{"name": "ali","email": "ali@mrsalehi.info"}' localhost:8000
curl -X DELETE -H "Content-type: application/json" -d'{"name": "ali","email": "ali@mrsalehi.info"}' localhost:8000

docker run --name backend -d -p 8000 -v ./data.json:/tmp/data.json backend:v0.1
```
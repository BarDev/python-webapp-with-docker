## Run using Python
```
pip install flask
python .\hello-world-api.py
```

## Run using pipenv
```
pipenv install flask
pipenv run python .\hello-world-api.py
```

---
## Test API Endpoints
Use "test.rest" to test api endpoints

### cUrl commands

```
curl --request GET \
  --url http://localhost:5000/hello \
  --header 'accept-encoding: gzip, deflate' \
  --header 'user-agent: vscode-restclient'
````
# Kiea Flask 2023

- [PyPi](https://pypi.org/)
- [Flask 2.2.3](https://pypi.org/project/Flask/)

- job
```
$ pip install flask
$ cat app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True, port=8080)

$ python app.py

```



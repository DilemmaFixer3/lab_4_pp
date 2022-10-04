from flask import Flask
from waitress import serve

app = Flask('__name__')

@app.route('/')
def index():
    return " "

@app.route('/api/v1/hello-world-1')
def hello_world():
    return "<h1>Hello World 1</h1>"


if __name__ == '__main__':
    #app.run(debug=True)
    serve(app)

#poetry run waitress-serve --listen=*:8000 main:app
#http://localhost:8000/api/v1/hello-world-1
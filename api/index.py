from flask import Flask

app = Flask(__name__)

@app.route('/test')
def index():
  return 'Hello World'

if __name__ == '__main__':
  app.run(host='localhost', port=8080)
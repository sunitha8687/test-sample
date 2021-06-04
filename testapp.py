from flask import Flask

app = Flask(__name__)


@app.route('/')
def demo():
  return "Heyyyyy, have a fantabulous day sunithaaaaa"

if __name__ == "__main__":
    app.run( debug = True, host="0.0.0.0", port = 80)

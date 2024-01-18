from flask import Flask

app = Flask(__name__)

# Definir uma rota raiz e a função que será executada
@app.route("/")
def hello_world():
  return "Hello World"

# Debug não deverá ser utilizado em PROD
if __name__ == "__main__":
  app.run(debug=True)

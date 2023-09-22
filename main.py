from flask import Flask, render_template, request 
from blueprints.helloworld.helloworld import helloworld_blueprint
from blueprints.calculator.calculator import calculator_blueprint


app = Flask(__name__)

app.register_blueprint(helloworld_blueprint)
app.register_blueprint(calculator_blueprint, url_prefix="/calculator")

if __name__ == "__main__":
    app.run(debug=True)
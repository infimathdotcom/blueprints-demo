from flask import Flask, render_template, redirect, url_for, Blueprint 

calculator_blueprint = Blueprint('calculator', __name__, template_folder='templates')

@calculator_blueprint.route('/')
def index():
    return "This is calculator bluprint." 


@calculator_blueprint.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}" 

@calculator_blueprint.route("/go_to_hello")
def go_to_hello():
    return redirect(url_for('hello_world.hello'))    


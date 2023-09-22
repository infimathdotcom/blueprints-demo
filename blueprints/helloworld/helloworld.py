from flask import Blueprint, render_template, request, redirect

helloworld_blueprint = Blueprint('hello_world', __name__, template_folder='templates')


@helloworld_blueprint.route('/')
def index():
    """return hello world"""
    return "Hello World"

@helloworld_blueprint.route('/hello')
def hello():
    """return hello world"""
    return "Hello World Again"

@helloworld_blueprint.route('/hello/<name>')
def hello_name(name):
    """return hello with argument name"""
    return f"Hello {name}!"

@helloworld_blueprint.route("/hellohtml")
def hellohtml():
    """returns the hello html file from templates directory"""
    return render_template('hello.html') 

from flask import flask
app=flask(__name__)
@pp.route('/')
def inicio():
    return("hola")
app.run(host='0.0.0.0')
    
import flask
from flask.app import Flask


from flask import Flask,redirect,url_for,render_template,request

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "TEST"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/api')

    return app
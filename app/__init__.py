#__init__ will bring our application together
from flask import Flask
app = Flask(__name__,template_folder='../templates',static_folder='../static')
app.secret_key='developedbysarakdahal9861392262'
app.config['TEMPLATES_AUTO_RELOAD'] = True
from app import user_views


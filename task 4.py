"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
from flask import Flask
from ApplicationContext import *
from Controllers.Admin.AdminController import *
from Controllers.HomePageController import *
from Controllers.AccountController import *
from Controllers.AlbumController import *
from DatabaseContext import db

db.create_all()

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

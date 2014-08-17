import flask, flask.views
import RPi.GPIO as GPIO, time
import os
import coffeeUtils

class Remote(flask.views.MethodView):

    def __init__(self):       
        self.coffeeIO=coffeeUtils.CoffeeIO()
        return

    def get(self):
        return flask.render_template('remote.html')
       

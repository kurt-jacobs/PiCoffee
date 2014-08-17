import flask, flask.views

class Remote(flask.views.MethodView):

    def __init__(self):       
        return

    def get(self):
        return flask.render_template('remote.html')
       

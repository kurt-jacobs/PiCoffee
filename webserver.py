# This is the flask server instance.
#
# To run:
#      sudo python webserver
#
# Kurt Jacobs
#
#--
#
# This work is free: you can redistribute it and/or modify it under the terms of Creative Commons Attribution ShareAlike license 
# v3.0
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the License for more details. You should have received a copy of the 
# License along
# with this program. If not, see <http://creativecommons.org/licenses/by-sa/3.0/>.


import flask
from flask import Flask, jsonify, request
import os
import dispatch

# Views
from main import Main
from remote import Remote

app = flask.Flask(__name__)
app.secret_key = os.urandom(24)

# Routes
app.add_url_rule('/',
                 view_func=Main.as_view('main'),
                 methods=["GET"])
app.add_url_rule('/<page>/',
                 view_func=Main.as_view('page'),
                 methods=["GET"])
app.add_url_rule('/remote/',
                 view_func=Remote.as_view('remote'),
                 methods=['GET', 'POST'])

@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404

@app.route('/remoteOpReq/', methods=['GET','POST'])
def remoteOpReq():
    ret_data = {"value": request.args.get('remoteOp')}
    status=dispatch.processRequest(ret_data["value"])
    ret_data["value"]=status;
    return jsonify(ret_data)

# change this value to match the IP of your PI
app.run(host='192.168.1.25',port=80 , debug=True)

"""
Author: Remy D <remyd@civx.us>
        Ralph Bean <rbean@redhat.com>
License: Apache 2.0
"""
import os

from flask import Flask
from flask.ext.mako import MakoTemplates, render_template

# This is how you Markdown in Flask according to the docs here:
# http://flask.pocoo.org/snippets/19/
#from flask.ext.markdown import Markdown
#Markdown(app)

app = Flask(__name__)
app.template_folder = "templates"
mako = MakoTemplates(app)

@app.route('/')
def index():
    return render_template('index.html', name='mako')



if __name__ == "__main__":
    if 'OPENSHIFT_PYTHON_IP' in os.environ:
        host = os.environ['OPENSHIFT_PYTHON_IP']
        port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
        app.run(host=host, port=port)
    else:
        app.debug = True
        app.run()

""" 
	INDEX ROUTES
"""
import os
from flask import abort, redirect, url_for, send_from_directory, current_app

from app.index import blueprint

@blueprint.route('/index')
@blueprint.route('/')
def index():
	""" set default route to authentication  """
	return redirect(url_for('authentication.login'))

@blueprint.route('/uploads/<string:directory>/<string:filename>')
def serve_file(directory, filename):
	""" for serving file upload  """
	uploads = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'] + "/{}/".format(directory))
	return send_from_directory(directory=uploads, filename=filename)
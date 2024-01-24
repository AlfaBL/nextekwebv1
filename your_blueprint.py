from flask import Blueprint, render_template, request, send_from_directory

your_blueprint = Blueprint('your_blueprint', __name__, template_folder='app/templates', static_folder='static')

@your_blueprint.route('/')
def index():
    return render_template('index.html')

@your_blueprint.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(your_blueprint.static_folder, filename)

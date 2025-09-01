from flask import Blueprint, request
from controllers.notebooks_controllers import create_notebook

notebooks_routes = Blueprint('notebook_routes', __name__)

@notebooks_routes.route('/Notebook', methods=['POST'])
def carros_post():
    notebook_data = request.json
    return create_notebook(request.json)
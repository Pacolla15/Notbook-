from models.notebooks_models import Notebook
from db import db
import json
from flask import make_response

def create_notebook(notebook_data):
    novo_notebook = Notebook(
        Nome=notebook_data['Nome'],
        Categoria=notebook_data['Categoria'],
        Preco=notebook_data['Preco']
    )
    db.session.add(novo_notebook)
    db.session.commit()
    response = make_response(
        json.dumps({
            'mensagem': 'Notebook adicionado successfully.',
            'carro': novo_notebook.json()
        }, sort_keys=False)
    )
    response.headers['content-Type'] = 'application/json'
    return response
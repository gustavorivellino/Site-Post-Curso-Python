from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario, Post

with app.app_context():
    database.create_all()

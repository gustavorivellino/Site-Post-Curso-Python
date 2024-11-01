from fakepinterest import app, database
from fakepinterest.models import User, Foto

with app.app_context():
    database.drop_all()
    database.create_all()
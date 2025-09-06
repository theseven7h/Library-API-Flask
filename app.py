from flask import Flask
from flask_pymongo import PyMongo

from controllers.author_controller import author_bp, init_author_controller
from data.repositories.author_repository import AuthorRepository
from services.author_services import AuthorServices
import controllers.error_handlers

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/libraryFlask'
mongo = PyMongo(app)

repository = AuthorRepository(mongo.db)
services = AuthorServices(repository)
init_author_controller(services)
app.register_blueprint(author_bp)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask_pymongo import PyMongo

from controllers.author_controller import author_bp, init_author_controller
from controllers.book_controller import book_bp, init_book_controller

from data.repositories.author_repository import AuthorRepository
from data.repositories.book_repository import BookRepository

from services.author_services import AuthorServices
from services.book_services import BookServices

import controllers.error_handlers

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/libraryFlask'
mongo = PyMongo(app)

author_repository = AuthorRepository(mongo.db)
book_repository = BookRepository(mongo.db)

author_services = AuthorServices(author_repository)
book_services = BookServices(book_repository)

init_author_controller(author_services)
init_book_controller(book_services)
app.register_blueprint(author_bp)
app.register_blueprint(book_bp)

if __name__ == '__main__':
    app.run(debug=True)
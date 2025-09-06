from flask import jsonify

from controllers.author_controller import author_bp
from controllers.book_controller import book_bp
from controllers.exceptions.exceptions import BookNotFoundException, EmptyUpdateException, AuthorNotFoundException
from datetime import datetime

@book_bp.errorhandler(BookNotFoundException)
def author_not_found(error):
    return jsonify({
        'error': error.message,
        'status': 404,
        'timestamp': datetime.now().isoformat()
    }), 404

@author_bp.errorhandler(EmptyUpdateException)
def empty_update(error):
    return jsonify({
        'error': error.message,
        'status': 400,
        'timestamp': datetime.now().isoformat()
    }), 400

@author_bp.errorhandler(AuthorNotFoundException)
def author_not_found(error):
    return jsonify({
        'error': error.message,
        'status': 404,
        'timestamp': datetime.now().isoformat()
    }), 404
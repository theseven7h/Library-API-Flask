from datetime import datetime

from flask import jsonify

from controllers.author_controller import author_bp
from utils.exceptions import AuthorNotFoundException, EmptyUpdateException
from datetime import datetime

@author_bp.errorhandler(AuthorNotFoundException)
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
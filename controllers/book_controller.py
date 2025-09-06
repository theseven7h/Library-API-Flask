from flask import Blueprint, request, jsonify

from dto.requests.add_book_request import BookRequest

book_bp = Blueprint('books', __name__, url_prefix='/books')

def init_book_controller(book_services):
    @book_bp.route('/add', methods=['POST'])
    def add_book():
        data = request.get_json()
        book_request = BookRequest(**data)
        response = book_services.add_book(book_request)
        return jsonify(response.to_dict()), 201

    @book_bp.route('', methods=['GET'])
    def get_all_books():
        books = book_services.get_all_books()
        return jsonify([book.to_dict() for book in books]), 200

    @book_bp.route('<book_id>', methods=['GET'])
    def get_book_by_id(book_id):
        book = book_services.get_book_by_id(book_id)
        return jsonify(book.to_dict()), 200

    @book_bp.route('<book_id>', methods=['PUT'])
    def update_book(book_id):
        data = request.get_json()
        book_request = BookRequest(**data)
        response = book_services.update_book(book_id, book_request)
        return jsonify(response.to_dict()), 200

    @book_bp.route('<book_id>', methods=['DELETE'])
    def delete_book(book_id):
        book_services.delete_book_by_id(book_id)
        return jsonify("Book deleted successfully"), 200


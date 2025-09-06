from flask import Blueprint, request, jsonify

from dto.requests.add_author_request import AuthorRequest

author_bp = Blueprint('author', __name__, url_prefix='/authors')

def init_author_controller(author_services):
    @author_bp.route('/add', methods=['POST'])
    def add_author():
        data = request.get_json()
        author_request = AuthorRequest(**data)
        response = author_services.add_author(author_request)
        return jsonify(response.to_dict()), 201

    @author_bp.route('', methods=['GET'])
    def get_all_authors():
        all_authors = author_services.get_all_authors()
        return jsonify([author.to_dict() for author in all_authors]), 200

    @author_bp.route('/<author_id>', methods=['GET'])
    def get_author_by_id(author_id):
        author = author_services.get_author_by_id(author_id)
        return jsonify(author.to_dict()), 200

    @author_bp.route('/<author_id>', methods=['PUT'])
    def update_author(author_id):
        data = request.get_json()
        author_request = AuthorRequest(**data)
        response = author_services.update_author(author_id, author_request)
        return jsonify(response.to_dict()), 200

    @author_bp.route('/<author_id>', methods=['DELETE'])
    def delete_author_by_id(author_id):
        author_services.delete_author_by_id(author_id)
        return jsonify("Author deleted successfully"), 200
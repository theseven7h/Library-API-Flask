from typing import Optional

from bson import ObjectId

from data.models.author import Author
from data.repositories import author_repository
from data.repositories.author_repository import AuthorRepository
from dto.requests.add_author_request import AuthorRequest
from utils.exceptions import AuthorNotFoundException, EmptyUpdateException
from utils.mapper import Mapper

class AuthorServices:
    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    def add_author(self, request: AuthorRequest):
        author = Mapper.map_to_author(request)
        author_id = self.author_repository.save(author)
        author.author_id = author_id
        return Mapper.map_to_response(author)

    def get_all_authors(self):
        all_authors = self.author_repository.find_all()
        return [Mapper.map_to_response(author) for author in all_authors]

    def get_author_by_id(self, author_id):
        author: Optional[Author] = self.author_repository.find_by_id(author_id)
        if not author:
            raise AuthorNotFoundException(f'Author with id {author_id} not found')
        return Mapper.map_to_response(author)

    def update_author(self, author_id, author_request):
        author = self.author_repository.find_by_id(ObjectId(author_id))
        if not author:
            raise AuthorNotFoundException(f'Author with id {author_id} not found')
        update = Mapper.map_to_author(author_request)
        updated_author = self.author_repository.update(ObjectId(author_id), update)
        if not updated_author:
            raise EmptyUpdateException("There is nothing to update")
        return Mapper.map_to_response(updated_author)


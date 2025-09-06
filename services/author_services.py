from typing import Optional

from bson import ObjectId

from data.models.author import Author
from data.repositories.author_repository import AuthorRepository
from dto.requests.add_author_request import AuthorRequest
from controllers.exceptions.exceptions import BookNotFoundException, EmptyUpdateException
from utils.mapper import Mapper


class AuthorServices:
    def __init__(self, repository: AuthorRepository):
        self.repository = repository

    def add_author(self, request: AuthorRequest):
        author = Mapper.map_to_author(request)
        author_id = self.repository.save(author)
        author.author_id = author_id
        return Mapper.map_to_author_response(self.repository.find_by_id(author_id))

    def get_all_authors(self):
        all_authors = self.repository.find_all()
        return [Mapper.map_to_author_response(author) for author in all_authors]

    def get_author_by_id(self, author_id):
        author: Optional[Author] = self.repository.find_by_id(author_id)
        if not author:
            raise BookNotFoundException(f'Author with id {author_id} not found')
        return Mapper.map_to_author_response(author)

    def update_author(self, author_id, author_request):
        author = self.repository.find_by_id(ObjectId(author_id))
        if not author:
            raise BookNotFoundException(f'Author with id {author_id} not found')
        update = Mapper.map_to_author(author_request)
        if not update.name and not update.bio:
            raise EmptyUpdateException("There is nothing to update")
        updated_author = self.repository.update(author_id, update)
        return Mapper.map_to_author_response(updated_author)

    def delete_author_by_id(self, author_id):
        author: Optional[Author] = self.repository.find_by_id(author_id)
        if not author:
            raise BookNotFoundException(f'Author with id {author_id} not found')
        self.repository.delete_by_id(author_id)
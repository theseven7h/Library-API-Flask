from bson import ObjectId

from controllers.exceptions.exceptions import BookNotFoundException, EmptyUpdateException
from data.models.book import Book
from data.repositories.book_repository import BookRepository
from dto.requests.add_book_request import BookRequest
from utils.mapper import Mapper


class BookServices:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def add_book(self, request: BookRequest):
        book = Mapper.map_to_book(request)
        book_id = self.repository.save(book)
        book.book_id = book_id
        return Mapper.map_to_book_response(self.repository.find_by_id(book_id))

    def get_all_books(self):
        books = self.repository.find_all()
        return [Mapper.map_to_book_response(book) for book in books]

    def get_book_by_id(self, book_id):
        book = self.repository.find_by_id(ObjectId(book_id))
        if not book:
            raise BookNotFoundException(f'Book with id {book_id} not found')
        return Mapper.map_to_book_response(book)

    def update_book(self, book_id, request: BookRequest):
        book = self.repository.find_by_id(ObjectId(book_id))
        if not book:
            raise BookNotFoundException(f'Book with id {book_id} not found')
        if not request.title and not request.genre and not request.author_id and not request.yearPublished:
            raise EmptyUpdateException(f'There is nothing to update')
        update = Mapper.map_to_book(request)
        updated_book = self.repository.update_book(ObjectId(book_id), update)
        return Mapper.map_to_book_response(updated_book)

    def delete_book_by_id(self, book_id):
        book = self.get_book_by_id(ObjectId(book_id))
        if not book:
            raise BookNotFoundException(f'Book with id {book_id} not found')
        self.repository.delete_book(book.book_id)
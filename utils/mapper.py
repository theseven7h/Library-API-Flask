from data.models.author import Author
from data.models.book import Book
from dto.requests.add_author_request import AuthorRequest
from dto.requests.add_book_request import BookRequest
from dto.responses.add_author_response import AddAuthorResponse
from dto.responses.add_book_response import AddBookResponse


class Mapper:
    @staticmethod
    def map_to_author(request: AuthorRequest):
        return Author(
            name = request.name,
            bio = request.bio
        )

    @staticmethod
    def map_to_author_response(saved_author):
        return AddAuthorResponse(
            author_id = saved_author.author_id,
            name = saved_author.name,
            bio = saved_author.bio
        )

    @staticmethod
    def map_to_book(request: BookRequest):
        return Book(
            title = request.title,
            genre = request.genre,
            author_id = request.author_id,
            yearPublished = request.yearPublished
        )

    @staticmethod
    def map_to_book_response(book: Book):
        return AddBookResponse(
            book_id = book.book_id,
            title=book.title,
            genre=book.genre,
            author_id=book.author_id,
            yearPublished=book.yearPublished
        )
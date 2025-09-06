from bson.objectid import ObjectId

from data.models.author import Author
from data.models.book import Book


class BookRepository:
    def __init__(self, db):
        self.db = db

    def save(self, book):
        return self.db.books.insert_one(book.to_dict()).inserted_id

    def find_all(self):
        return [Book.from_dict(book) for book in self.db.books.find()]

    def find_by_id(self, book_id):
        document = self.db.books.find_one({'_id': ObjectId(book_id)})
        return Book.from_dict(document) if document else None


    def update_book(self, book_id, book):
        updated_details = self.__check_book(book)
        self.db.books.update_one({'_id': ObjectId(book_id)}, {'$set': updated_details})
        return self.find_by_id(book_id)

    def __check_book(self, book):
        if not book:
            return None
        ready_book = {}
        if book.title:
            ready_book['title'] = book.title
        if book.genre:
            ready_book['genre'] = book.genre
        if book.yearPublished:
            ready_book['yearPublished'] = book.yearPublished
        if book.author_id:
            ready_book['author_id'] = book.author_id
        return ready_book

    def delete_book(self, book_id):
        self.db.books.delete_one({'_id': ObjectId(book_id)})